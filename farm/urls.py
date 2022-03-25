from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
app_name = 'farm'
urlpatterns = [
    path('my-farms/',views.farm_list,name='farm_list'),
    path('farm-detail/<int:id>/',views.farm_detail, name='farm_detail'),
    path('edit-farm/<int:id>/',views.farm_edit, name='farm_edit'),
    path('add_farm/',views.add_farm, name='add_farm'),
] 