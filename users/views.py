from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created Successfully")
            return redirect('home')

    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    context = {
    'title': 'Profile',
    }
    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
def update_profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Profile updated Successfully')
            return redirect('profile')

    else:
        p_form = ProfileUpdateForm()

    context = {
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html', context)
