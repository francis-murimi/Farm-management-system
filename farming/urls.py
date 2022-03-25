from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
app_name = 'farming'
urlpatterns = [
    path('crop-farming/<int:id>/',views.crop_farming, name='crop_farming'),
    path('animal-farming/<int:id>/',views.animal_farming, name='animal_farming'),
    path('add-crop-harvest/<int:id>/',views.crop_harvest, name='crop_harvest'),
    path('add-animal-harvest/<int:id>/',views.animal_harvest, name='animal_harvest'),
    path('finish-crop-mission/<int:id>/',views.finish_crop_mission, name='finish_crop_mission'),
    path('finish-animal-mission/<int:id>/',views.finish_animal_mission, name='finish_animal_mission'),
    path('sell-crop/<int:id>/',views.sell_crop, name='sell_crop'),
    path('sell-animal/<int:id>/',views.sell_animal, name='sell_animal'),
] 