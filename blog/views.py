from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Article, Categorie

# Create your views here.
def index (request):
    name = Article.objects.all()
    return render(request, 'blog/index.html', {'name': name})

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_Article_list'
    
    def get_queryset(self):
        """
        Return the last five published Articles (not including those set to be
        published in the future).
        """
        return Article.objects.filter()