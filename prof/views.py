from django.shortcuts import render


def yo_profile(request):
    return render(request, 'prof/yo_profile.html')
