from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Article, Categorie

# Create your views here.
def index (request):
    name = Article.objects.all()
    return render(request, 'blog/index.html', {'name': name})




def un_article(request, id):
    affiche= Article.objects.get(pk=id)
    return render(request, 'blog/all_articles.html', {"affiche":affiche})