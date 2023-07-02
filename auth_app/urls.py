from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name='auth_app'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logoff', LogoutView.as_view(), name='logoff'),
]
