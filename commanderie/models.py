from django.db import models
from django.utils.translation import gettext as _
from districte.models import Section
# Create your models here.

class Commanderie(models.Model):
    name = models.CharField("nom commanderie",max_length=100, blank=True, null=True)
    numero = models.PositiveSmallIntegerField(_("numéro commanderie"))
    date = models.DateField(_("date de création"), auto_now=False)
    adresse = models.CharField("adresse",max_length=100, blank=True, null=True)
    telephone = models.CharField("telephone", max_length=11, blank=True, null=True)
    email= models.EmailField(_("couriel"), max_length=254)
    sections = models.ForeignKey(Section, related_name='section', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Commanderie")
        verbose_name_plural = _("Commanderies")
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Commanderie_detail",kwargs={"pk": self.pk})
    







TYPE_CHEVALIER= (
    ('CHEVALIER', 'CHEVALIER'),
    ('DAME OXILLIAIRE', 'DAME OXILLIAIRE'),
    ('JUNIOR', 'JUNIOR'),
    ('SENIOR', 'SENIOR'),
) 

TYPE_GARDE= (
    ('MAJOR', 'MAJOR'),
    ('BRIGADIER GENERAL', 'BRIGADIER GENERAL'),
    ('OFFICIE', 'OFFICIE'),
) 

class Chevalier(models.Model):
    fisrt_name = models.CharField("nom",max_length=100, blank=False, null=False)
    last_name = models.CharField("prénom",max_length=100, blank=False, null=False)
    type_chevalier= models.CharField("type de chevalier", max_length=100, choices =TYPE_CHEVALIER, default=[0])
    grade_chevalier= models.CharField("type de grade", max_length=100, choices= TYPE_GARDE, default=[0])
    date = models.DateField(_("date d'initiation"), auto_now=False, blank=False, null=False)
    telephone = models.CharField("telephone",max_length=11, blank=False, null=False)
    adresse = models.CharField("adresse",max_length=100, blank=False, null=False)
    profession = models.CharField("profession",max_length=100, blank=False, null=False)
    commanderie = models.ForeignKey(Commanderie, related_name='commanderie', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Chevalier")
        verbose_name_plural = _("Chevaliers")

    def __str__(self):
        return self.fisrt_name

    def get_absolute_url(self):
        return reverse("chevalier_detail", kwargs={"pk": self.pk})
    

    
class Bureau(models.Model):
    president =  models.CharField("président", max_length=100, blank=True, null=True )
    vice_president =  models.CharField("vice président", max_length=100, blank=True, null=True )
    secrtaire =  models.CharField("secretaire", max_length=100, blank=True, null=True )
    vice_secretaire = models.CharField("vice secretaire", max_length=100, blank=True, null=True )
    tresorier = models.CharField("tresorier", max_length=100, blank=True, null=True )
    vice_tresorier =  models.CharField("vice tresorier", max_length=100, blank=True, null=True )
    date = models.DateField(_("date d'installation"), auto_now=False)
    commanderie =  models.ForeignKey(Commanderie, verbose_name='commanderie', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Bureau")
        verbose_name_plural = _("Bureaux")

    def __str__(self):
        return self.president

    def get_absolute_url(self):
        return reverse("bureau_detail", kwargs={"pk": self.pk})

        
