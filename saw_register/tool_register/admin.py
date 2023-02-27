from django.contrib import admin
from .models import *



@admin.register(SawBrand)
class SawBrandAdmin(admin.ModelAdmin):
    # list_display = ('pavadinimas', 'date_created', 'date_modified')
    pass

@admin.register(Saw)
class SawAdmin(admin.ModelAdmin):
    # list_display = ('pavadinimas', 'date_created', 'date_modified')
    pass

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('saw', 'metres', 'date_created', 'date_modified')
    pass

@admin.register(WorkPlace)
class WorkPlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass








