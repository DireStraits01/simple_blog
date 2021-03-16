from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.conf import settings
from .models import Profile


def profilePage(request, id):
    profile = Profile.objects.get(id=id)
    context = {'profile':profile}
    return render(request, 'prof/profilePage.html', context )

########______________authenticated___________________#########
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                print('error username')
                messages.info(request, "username is already taken")
                return redirect('register')

            elif User.objects.filter(email=email):
                print('error email')
                messages.info(request, 'email is already taken')
                return redirect('register')

            else:
                User.objects.create_user(
                    username=username, email=email,
                    password=password1)
                user = auth.authenticate(username=username, password=password1)
                user.refresh_from_db()
                user.save()
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, "password not confirm")
            return redirect('register')
    return render(request, 'prof/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        try:
            remember = request.POST['remember_me']
            if remember:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        except:
            is_private = False
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'prof/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
