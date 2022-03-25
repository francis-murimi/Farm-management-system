from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
app_name = 'management'
urlpatterns = [
    path('crop-list/',views.crop_list, name='crop_list'),
    path('crop-detail/<int:id>/',views.crop_detail, name='crop_detail'),
    path('animal-list/',views.animal_list, name='animal_list'),
    path('animal-detail/<int:id>/',views.animal_detail, name='animal_detail'),
    ]