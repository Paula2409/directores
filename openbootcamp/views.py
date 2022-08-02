from django.shortcuts import render
from django.views import generic
from openbootcamp.models import Directores

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Directores
