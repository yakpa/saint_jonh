from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(" name", max_length=100, blank=True, null=True)
    
    

    class Meta:
        verbose_name = _("Categorie")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categorie_detail", kwargs={"pk": self.pk})
    
class Article(models.Model):
    name = models.CharField("nom de l'articles", max_length=100, blank=True, null=True)
    models.DateTimeField(_("date de publication"), auto_now=False)
    categories = models.ForeignKey(Categorie, related_name='categories', on_delete=models.CASCADE)
    
    
    

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


