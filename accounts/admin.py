from django.contrib import admin
from . models import County,Ward,Farmer

class CountyAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(County,CountyAdmin)

class WardAdmin(admin.ModelAdmin):
    list_display = ['name','county']
    list_filter = ['county']
admin.site.register(Ward,WardAdmin)

class FarmerAdmin(admin.ModelAdmin):
    list_display = ['user','county','ward','gender']
    list_filter = ['county','ward','gender','disability']
admin.site.register(Farmer,FarmerAdmin)