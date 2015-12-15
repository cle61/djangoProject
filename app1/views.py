from django.shortcuts import render
from django.http import HttpResponse

from .models import Cat

import pprint

# Create your views here.

def home(request):
	"""Page d'accueil"""
	text = "<h1>HELLO WORLD</h1>"
	return HttpResponse(text)

def cat(request, cat_id):
    try:
        cat = Cat.objects.get(pk=cat_id)
    except Cat.DoesNotExist:
        raise Http404("Cat does not exist")
    return render(request, 'cat.html', {'cat': cat})

def cats(request):
    cat_list = Cat.objects.all()
    output = ', '.join([q.cat_name for q in cat_list])
    return HttpResponse(output)