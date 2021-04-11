from django.shortcuts import render, redirect
from bookapp.forms import AfegirLlibreForm
from users.admin import CustomUserAdmin
from users.forms import CustomUserCreationForm, SignUpForm
def homePage(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
	

def afegirLlibre(request):
    if request.method == 'POST':
        form = AfegirLlibreForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.escriptor = request.user
            obj.save()
            return redirect('afegirllibre')
    else:
        form = AfegirLlibreForm()
    return render(request, "comments.html", {'form': form})

