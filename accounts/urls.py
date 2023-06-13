from django.urls import path
from rest_framework.authtoken import views

app_name="accounts"
urlpatterns = [
    path('auth', views.obtain_auth_token, name="auth")
]