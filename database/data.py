import pandas as pd
import psycopg2

db_config = {
    "dbname":"cache_db",
    "host":"localhost",
    "port":5432,
    "password":"user_password",
    "user":"db_user"
}

def database_connection():
    return psycopg2.connect(**db_config)

def create_table(conn, name, columns):
    with conn.cursor() as cur:
        cur.execute(f"create table if not exists {name} ({','.join(columns)})")

def insert_data(conn,table,data):
    with conn.cursor() as cur:
        cols = ",".join(data.columns)
        for row in data.itertuples(index=False):
            cur.execute(f"insert into {table} ({cols}) values ({','.join(['%s'] * len(row))})", row)
    conn.commit()

def populate_database_table():
    table_name = "superstore"
    columns = ["OrderID varchar(255)","OrderDate date","ShipDate date","ShipMode varchar(255)","CustomerID varchar(255)","CustomerName varchar(255)","Segment varchar(255)","Country varchar(255)","City varchar(255)","State varchar(255)","PostalCode varchar(255)","Region varchar(255)","ProductID varchar(255)","Category varchar(255)","SubCategory varchar(255)","ProductName varchar(255)","Sales float"]
    dataset = "./database/train.csv"
    df = pd.read_csv(dataset)
    df.drop(["Row ID","Unnamed: 18"],axis=1,inplace=True)
    df = df[df['Product Name'] != "Imation Secure+ Hardware Encrypted USB 2.0 Flash Drive"]
    df.columns = ["OrderID","OrderDate","ShipDate","ShipMode","CustomerID","CustomerName","Segment","Country","City","State","PostalCode","Region","ProductID","Category","SubCategory","ProductName","Sales"]
    df["OrderDate"] = pd.to_datetime(df["OrderDate"],format="%d/%m/%Y")
    df["ShipDate"] = pd.to_datetime(df["ShipDate"],format="%d/%m/%Y")
    
    db_conn = database_connection()
    create_table(db_conn,table_name,columns)
    insert_data(db_conn,table_name,df)
    db_conn.close()

if __name__ == "__main__":
    populate_database_table()