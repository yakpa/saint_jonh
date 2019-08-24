from django.shortcuts import render

# Create your views here.
def index (request):
    nom = Article.objects.all()
    return render(request, {'nom': nom})