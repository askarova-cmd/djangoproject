from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


def index(request):
    return render(request, 'kazakhfood/index.html')


def about(request):
    return render(request, 'kazakhfood/about.html')


def menu(request):
    return render(request, 'kazakhfood/about.html')


def blog(request):
    return render(request, 'kazakhfood/about.html')


def login_view(request):
    return render(request, 'kazakhfood/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                auth_login(request, user)
                return redirect("index")
            else:
                return render(request, "kazakhfood/register.html", {
                    "error": "Пользователь уже существует"
                })
        else:
            return render(request, "kazakhfood/register.html", {
                "error": "Пароли не совпадают"
            })

    return render(request, "kazakhfood/register.html")


def reserve(request):
    return render(request, 'kazakhfood/reserve.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "kazakhfood/contacts.html", {
            "success": True
        })

    return render(request, "kazakhfood/contacts.html")
















