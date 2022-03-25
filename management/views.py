from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from farming.models import MissionP, MissionA, Plant_Harvest, Animal_Harvest
from accounts.models import Farmer
from farm.models import Farm, Crop, Animal
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Min, Sum
from .forms import WardForm

def crop_list(request): 
    crops = Crop.objects.all()
    context = {'crops':crops}
    template = loader.get_template('management/crop_list.html')
    return HttpResponse(template.render(context,request))

def crop_detail(request,id): 
    crop = get_object_or_404(Crop,id=id)
    if request.method == 'POST':
        form =WardForm(request.POST,) 
        if form.is_valid(): 
            ward_name = form.cleaned_data.get('name')
            complete_missions = MissionP.objects.filter(crop=crop,complete=1,ward=ward_name).count()
            incomplete_missions = MissionP.objects.filter(crop=crop,complete=0,ward=ward_name).count()
            sold_harvests = Plant_Harvest.objects.filter(crop=crop,sold=1,ward=ward_name).aggregate(Sum('quantity'))
            unsold_harvests = Plant_Harvest.objects.filter(crop=crop,sold=0,ward=ward_name).aggregate(Sum('quantity'))
            mission = MissionP.objects.filter(crop=crop,complete=0,ward=ward_name)
            farms = []
            for m in mission:  
                farms.append(m.farm.farm_size)
            farm_total = sum(farms)
    else: 
        form = WardForm() 
        complete_missions = MissionP.objects.filter(crop=crop,complete=1).count()
        incomplete_missions = MissionP.objects.filter(crop=crop,complete=0).count()
        sold_harvests = Plant_Harvest.objects.filter(crop=crop,sold=1).aggregate(Sum('quantity'))
        unsold_harvests = Plant_Harvest.objects.filter(crop=crop,sold=0).aggregate(Sum('quantity'))
        mission = MissionP.objects.filter(crop=crop,complete=0)
        farms = []
        for m in mission:  
            farms.append(m.farm.farm_size)
        farm_total = sum(farms)
    context = {'crop':crop,'form':form,
                'complete_missions':complete_missions,'incomplete_missions':incomplete_missions,
                'sold_harvests':sold_harvests,'unsold_harvests':unsold_harvests,
                'farm_total':farm_total}
    template = loader.get_template('management/crop_detail.html')
    return HttpResponse(template.render(context,request))


def animal_list(request): 
    animals = Animal.objects.all()
    context = {'animals':animals}
    template = loader.get_template('management/animal_list.html')
    return HttpResponse(template.render(context,request))

def animal_detail(request,id): 
    animal = get_object_or_404(Animal,id=id)
    if request.method == 'POST':
        form =WardForm(request.POST,) 
        if form.is_valid(): 
            ward_name = form.cleaned_data.get('name')
            complete_missions = MissionA.objects.filter(animal=animal,complete=1,ward=ward_name).count()
            incomplete_missions = MissionA.objects.filter(animal=animal,complete=0,ward=ward_name).count()
            sold_harvests = Animal_Harvest.objects.filter(animal=animal,sold=1,ward=ward_name).aggregate(Sum('quantity'))
            unsold_harvests = Animal_Harvest.objects.filter(animal=animal,sold=0,ward=ward_name).aggregate(Sum('quantity'))
            mission = MissionA.objects.filter(animal=animal,complete=0,ward=ward_name)
            farms = []
            for m in mission:  
                farms.append(m.farm.farm_size)
            farm_total = sum(farms)
    else: 
        form = WardForm() 
        complete_missions = MissionA.objects.filter(animal=animal,complete=1).count()
        incomplete_missions = MissionA.objects.filter(animal=animal,complete=0).count()
        sold_harvests = Animal_Harvest.objects.filter(animal=animal,sold=1).aggregate(Sum('quantity'))
        unsold_harvests = Animal_Harvest.objects.filter(animal=animal,sold=0).aggregate(Sum('quantity'))
        mission = MissionA.objects.filter(animal=animal,complete=0)
        farms = []
        for m in mission:  
            farms.append(m.farm.farm_size)
        farm_total = sum(farms)
    context = {'animal':animal,'form':form,
                'complete_missions':complete_missions,'incomplete_missions':incomplete_missions,
                'sold_harvests':sold_harvests,'unsold_harvests':unsold_harvests,
                'farm_total':farm_total}
    template = loader.get_template('management/animal_detail.html')
    return HttpResponse(template.render(context,request))