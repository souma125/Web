from django.urls import path,include
from main import views
urlpatterns = [
    path('', views.register,name="register"),
    path('register', views.register,name="register"),
    path('cars', views.cars,name="cars"),
]