from django.urls import path
from . views.auth import CustomAuthToken

app_name="accounts"
urlpatterns = [
    path('auth', CustomAuthToken.as_view(), name="auth")
]