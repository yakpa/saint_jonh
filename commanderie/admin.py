from django.contrib import admin
from commanderie.models import Bureau, Chevalier, Commanderie

# Register your models here.
admin.site.register(Commanderie)
admin.site.register(Chevalier)
admin.site.register(Bureau)
