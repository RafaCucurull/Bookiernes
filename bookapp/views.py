from django.shortcuts import render, redirect
from bookapp.forms import AfegirLlibreForm
from users.models import CustomUser


def homePage(request):
    return render(request, "home.html")


def Escriptori(request):
    usuari=CustomUser.objects.get(email=request.user)
    if not usuari.is_Treballador:
        return render(request, "home.html")
    else:
        if usuari.is_Escriptor:
            return render(request, "home.html")
        if usuari.is_Editor:
            return render(request, "home.html")


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
