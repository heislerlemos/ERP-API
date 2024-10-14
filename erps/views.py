from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from erps.models import Rh

def erps(request):
    
    rhs = Rh.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'myerps' : rhs,
    }
    return HttpResponse(template.render(context, request))


