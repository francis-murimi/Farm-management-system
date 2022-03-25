from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('',views.home,name ='home'),
    path('farmer-register/',views.farmer_register,name='farmer_register'),
    path('login/',views.log_in,name='log_in'),
    path('logout/',views.log_out,name='log_out'), 
    path('user-check',views.check_user,name='check_user'), 
] 