from django.shortcuts import render, HttpResponse
from .models import Vaca

# Create your views here.

def listado(request):
    #select * from
    vaca = Vaca.objects.all()
    return render(request, "vacuno/listado.html", {'vc':vaca})
