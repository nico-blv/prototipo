from django.contrib import admin
from .models import Vaca

# Register your models here.

class VacasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Vaca, VacasAdmin)
