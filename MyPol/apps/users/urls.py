from django.urls import path, include 
from apps.users import views

urlpatterns=[
    path('', views.welcome, name="welcome"),
    path('register/', views.register,name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]