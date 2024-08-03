from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import Account

# Create your views here.


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Account.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists.")
            return redirect("signup")
        else:
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
    else:
        return render(request, "register/signup.html")


def login(request):
    return render(request, "register/login.html")


def logout(request):
    pass
