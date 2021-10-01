from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, UpdateForm, UserUpdateForm
from django.contrib import messages
from .models import Details
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, "home.html")


def registration(request):
    form = RegistrationForm()
    context = {"form": form}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created")
            return redirect("login")
        else:
            context["form"] = form
            return render(request, "registration.html", context)

    return render(request, "registration.html", context)


def signin(request):
    form = LoginForm()
    context = {"form": form}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                context = {"form": form}
                return render(request, "login.html", context)

    return render(request, "login.html", context)


@login_required
def update_details(request):
    detail=Details.objects.get(id=5)
    print(detail)
    p_form = UpdateForm(instance=detail)
    u_form = UserUpdateForm(instance=request.user)
    if request.method == "GET":
        context = {"u_form": u_form, "p_form": p_form}
        return render(request, "update_details.html", context)
    elif request.method == "POST":
        p_form = UpdateForm(request.POST, request.FILES)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, "Details updated successfully")
            return redirect("home")
        else:
            context = {"u_form": u_form, "p_form": p_form}
            return render(request, "update_details.html", context)


def list_details(request):
    detail = Details.objects.get(id=5)
    context = {"detail": detail}
    return render(request, "my_profile.html", context)


def signout(request):
    logout(request)
    return redirect("signin")
