from django.contrib import admin
from .models import Farm, Crop, Animal

class FarmAdmin(admin.ModelAdmin):
    list_display = ['county','ward','farm_size','farmer']
    list_filter = ['county','ward','water_availability']
admin.site.register(Farm,FarmAdmin)

class CropAdmin(admin.ModelAdmin): 
    list_display = ['name','crop_type']
    list_filter = ['crop_type','crop_product','crop_growth']
admin.site.register(Crop,CropAdmin)

class AnimalAdmin(admin.ModelAdmin): 
    list_display = ['name','animal_product']
    list_filter = ['animal_product','maturity_age','animal_feed']
admin.site.register(Animal, AnimalAdmin)
