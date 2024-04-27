from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authentication successful!')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    form = LoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context=context)


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {'section': 'dashboard'})

@login_required
def signout(request):
    logout(request)
    return render(request, "registration/logged_out.html")

