from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth import login, authenticate
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def index(request):
    return render(request, 'instagram/index.html')

@login_required(login_url='login')
def profile(request, username):
    user_form = UpdateUserForm()
    prof_form = UpdateUserProfileForm()
    params = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'instagram/profile.html', params)
