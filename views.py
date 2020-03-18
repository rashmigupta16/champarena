from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    return render(request, 'startup/index.html')


def special(request):
    return HttpResponse("You are logged in !")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()

    else:
        user_form = SignUpForm()
    return render(request, 'startup/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'startup/login.html', {})
