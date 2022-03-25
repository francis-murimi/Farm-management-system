from django.contrib import admin
from .models import MissionA,MissionP,Animal_Harvest,Plant_Harvest
from farm.models import Farm
from accounts.models import Ward

class MissionAAdmin(admin.ModelAdmin): 
    list_display = ['farmer','ward','start_time','complete']
    list_filter = ['complete','ward']
admin.site.register(MissionA,MissionAAdmin)

class MissionPAdmin(admin.ModelAdmin): 
    list_display = ['farmer','ward','start_time','complete']
    list_filter = ['complete','ward']
admin.site.register(MissionP,MissionPAdmin)

class Plant_HarvestAdmin(admin.ModelAdmin): 
    list_display = ['farmer','ward','crop','quantity']
    list_filter = ['crop','sold','ward']
admin.site.register(Plant_Harvest,Plant_HarvestAdmin)

class Animal_HarvestAdmin(admin.ModelAdmin): 
    list_display = ['farmer','ward','animal','quantity']
    list_filter = ['animal','ward','sold']
admin.site.register(Animal_Harvest,Animal_HarvestAdmin)

