from django.shortcuts import render

def mapa_view(request):
    return render(request, 'alvos/index.html') 