from unicodedata import name
from django.urls import path 
from cryptoapp import views

urlpatterns = [
    path('login',views.login,name="login"),
]