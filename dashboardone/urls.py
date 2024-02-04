from django.urls import path
from dashboardone import views


urlpatterns = [
    path("", views.index, name="home"),
    path("analytics/", views.analytics, name="analytics"),
    path("reports/", views.reports, name="reports"),
]