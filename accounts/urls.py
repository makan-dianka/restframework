from django.urls import path
from . views.auth import CustomAuthToken
from .views import create_user, user_profile

app_name="accounts"
urlpatterns = [
    path('auth', CustomAuthToken.as_view(), name="auth"),
    path('create_user', create_user.create_user, name="create_user"),
    path('profile', user_profile.profile, name="profile"),
]