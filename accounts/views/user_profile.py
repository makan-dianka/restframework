from django.shortcuts import render
from rest_framework.authtoken.models import Token
from .. models import CustomUser


def profile(request):
    context = {}
    if request.user.is_authenticated:
        user = CustomUser.objects.get(pk=request.user.id)
        token = Token.objects.get(user=user)
        context['token']=token.key
    return render(request, "accounts/profile.html", context)