from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .models import Cat, Cat_color

from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

import pprint

# Create your views here.

def home(request):
    cat_list = Cat.objects.all()[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'cat_list': cat_list,
    })
    return HttpResponse(template.render(context))

def cat(request, cat_id):
    try:
        cat = Cat.objects.get(pk=cat_id)
        cat_color = Cat_color.objects.get(pk=cat.cat_color.pk)
    except Cat.DoesNotExist:
        raise Http404("Cat does not exist")
    return render(request, 'cat.html', {'cat': cat, 'cat_color': cat_color})

def cats(request):
    cat_list = Cat.objects.all()
    template = loader.get_template('cats.html')
    context = RequestContext(request, {
        'cat_list': cat_list,
    })
    return HttpResponse(template.render(context))

def add_cat(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addCatForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addCatForm()

    return render(request, 'addCat.html', {'form': form})

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes

            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur

            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/')