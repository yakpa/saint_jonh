from django.contrib import admin
from blog.models import Categorie, Article

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article)