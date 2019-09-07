from django.shortcuts import render

# Create your views here.
def commandview (request, command):
    nomprod = Article.objects.all()
    return render(request, {'nomprod': nomprod})
