from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import (
    RegisterForm,
    ProfileForm,
    LoginForm
)


# =========================================================
# HOME
# =========================================================

def home(request):

    return render(
        request,
        'home.html'
    )


# =========================================================
# ABOUT
# =========================================================

def about(request):

    return render(
        request,
        'about.html'
    )


# =========================================================
# REGISTER
# =========================================================

def register(request):

    if request.method == 'POST':

        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            profile.save()

            login(
                request,
                user
            )

            messages.success(
                request,
                'Registration successful.'
            )

            return redirect('home')

    else:

        user_form = RegisterForm()
        profile_form = ProfileForm()

    return render(
        request,
        'register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    )


# =========================================================
# LOGIN
# =========================================================

def login_view(request):

    if request.method == 'POST':

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user
            )

            return redirect('home')

    else:

        form = LoginForm()

    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )


# =========================================================
# LOGOUT
# =========================================================

def logout_view(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out.'
    )

    return redirect('login')