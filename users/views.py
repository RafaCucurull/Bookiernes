from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import CustomUserCreationForm, CustomLectorCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            user.is_Treballador = True
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def registerLector(request):
    if request.method == 'POST':
        form = CustomLectorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_Subscrit = True
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomLectorCreationForm()
    return render(request, 'registration/register_lector.html', {'form': form})
