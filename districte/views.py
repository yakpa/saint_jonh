from django.shortcuts import render

# Create your views here.
def indexdist (request):
    nom = Article.objects.all()
    return render(request, {'nom': nom})