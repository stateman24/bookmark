from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm


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


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            context = {'user': user}
            return render(request, 'account/register_done.html', context)
    else:
        form = UserRegistrationForm()
        context = {'form': form}
        return render(request, 'account/register.html', context)

