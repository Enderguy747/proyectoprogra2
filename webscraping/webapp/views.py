from django.shortcuts import render,redirect
from.models import Citas
from .excecute import Execute


# Create your views here.
def index(request):
    CitaObj = Citas.objects.all()
    context = {'citas':CitaObj}
    return render(request, 'webapp/quotes.html',context)


def scrapear(request):
    scrap = Execute()
    scrap.EjecutarSpider()
    return redirect('index')
