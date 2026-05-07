from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from members.forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    context = {
        "form":form
    }
    return render(request, "register.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request , user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    context = {
        "form":form
    }
    return render(request, "login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("login")