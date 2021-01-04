from django.shortcuts import render


def yo_profile(request):
    return render(request, 'prof/yo_profile.html')


def login_page(request):
    return render(request, 'prof/login_page.html')


def registration_page(request):
    return render(request, 'prof/registration_page.html')
