from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def connexion(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.info(request, 'email ou mot de passe est incorrect')
    return render(request, 'accounts/login.html')

def logoutpage(request):
    logout(request)
    return redirect('accounts:connexion')
