from django.shortcuts import render


def yo_profile(request):
    return render(request, 'prof/yo_profile.html')


def login(request):
    return render(request, 'prof/login.html')


def registration(request):
    return render(request, 'prof/registration.html')
