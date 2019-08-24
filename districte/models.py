from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Districte(models.Model):
    name = models.CharField("nom districte", max_length=100, blank=True, null=True)
    date = models.DateField(_("date de création"), auto_now=False)
    adresse = models.CharField("adresse",max_length=100, blank=True, null=True)
    telephone = models.CharField("telephone", max_length=11, blank=True, null=True)
    email= models.EmailField(_("couriel"), max_length=254)
    

    class Meta:
        verbose_name = _("Districte")
        verbose_name_plural = _("Districtes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("districte_detail", kwargs={"pk": self.pk})

class Section(models.Model):
    name = models.CharField("nom section",max_length=100, blank=True, null=True)
    date = models.DateField(_("date de création"), auto_now=False)
    adresse = models.CharField("adresse",max_length=100, blank=True, null=True)
    telephone = models.CharField("telephone", max_length=11, blank=True, null=True)
    email= models.EmailField(_("couriel"), max_length=254)
    districtes = models.ForeignKey(Districte, verbose_name='districte', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("section_detail", kwargs={"pk": self.pk})
