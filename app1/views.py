from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
	"""Page d'accueil"""
	text = "<h1>HELLO WORLD</h1>"
	return HttpResponse(text)

def hello(request, name):
	"""Page d'accueil"""
	text = "<h1>HELLO #{0} !</h1>".format(name)
	return HttpResponse(text)