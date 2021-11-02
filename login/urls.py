from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.welcome, name="welcome"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('lab', views.lab, name="lab"),
    path('reports', views.reports, name="reports"),
    path('staff', views.staffManagement, name="staff"),
    path('patients', views.patients, name="patients"),

]
