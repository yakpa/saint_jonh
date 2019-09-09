from django.urls import path
from .import views as blog

app_name="blog"
urlpatterns = [
         path('', blog.index, name='index'),
         path('un_article/<int:id>', blog.un_article, name='un_article'),
]