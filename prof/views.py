from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib import messages


def yo_profile(request):
    return render(request, 'prof/yo_profile.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'prof/login.html')


def registr(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()

            return render(request, 'prof/register_done.html')
    else:
        user_form = UserCreationForm()
    context = {'user_form': user_form}
    return render(request, 'prof/registration.html', context)
