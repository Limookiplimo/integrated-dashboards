from django.urls import path
from dashboardone import views


urlpatterns = [
    path('', views.index, name='home')
]