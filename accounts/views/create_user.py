from django.shortcuts import render, redirect
from .. forms import CustomUserCreationForm
from django.contrib import messages


def create_user(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile")
        else:
            messages.error(request, "erreur : les saisis ne sont pas valide. Assurez-vous d'utiliser un mot de passe fort et identique ou essayer avec un autre adresse mail")
    form = CustomUserCreationForm
    context = {'form' : form}
    return render(request, "accounts/create_user.html", context)