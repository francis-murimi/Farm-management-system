from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import MissionP, MissionA, Plant_Harvest, Animal_Harvest
from .forms import MissionPForm, MissionAForm,  Plant_HarvestForm, Animal_HarvestForm
from accounts.models import Farmer
from farm.models import Farm, Crop, Animal
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def crop_farming(request,id):  
    farm = get_object_or_404(Farm,id=id)
    i_d=''
    if request.method == 'POST':
        form = MissionPForm (request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.farmer = farm.farmer
            mission.ward = farm.ward
            mission.farm = farm
            mission.save()
            i_d=farm.id
            return redirect('farm:farm_detail',id=i_d)
    else:
        form = MissionPForm()
    context = {'form':form}
    template = loader.get_template('farming/crop_farming.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/login/')
def animal_farming(request,id):  
    farm = get_object_or_404(Farm,id=id)
    i_d = ''
    if request.method == 'POST':
        form = MissionAForm (request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.farmer = farm.farmer
            mission.farm = farm
            mission.ward = farm.ward
            mission.save()
            i_d = farm.id
            return redirect('farm:farm_detail',id=i_d)
    else:
        form = MissionAForm()
    context = {'form':form}
    template = loader.get_template('farming/animal_farming.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/login/')
def crop_harvest(request, id):
    mission = get_object_or_404(MissionP,id=id)
    i_d=mission.farm.id
    if request.method == 'POST':
        form = Plant_HarvestForm (request.POST)
        if form.is_valid():
            harvest = form.save(commit=False)
            harvest.farmer = mission.farm.farmer
            harvest.mission = mission
            harvest.farm = mission.farm
            harvest.ward = mission.farm.ward
            harvest.crop = mission.crop 
            harvest.save()
            return redirect('farm:farm_detail',id=i_d)
    else:
        form = Plant_HarvestForm()
    context = {'form':form}
    template = loader.get_template('farming/crop_harvest.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/login/')
def animal_harvest(request, id):
    mission = get_object_or_404(MissionA,id=id)
    i_d=mission.farm.id
    if request.method == 'POST':
        form = Animal_HarvestForm (request.POST)
        if form.is_valid():
            harvest = form.save(commit=False)
            harvest.farmer = mission.farm.farmer
            harvest.farm = mission.farm
            harvest.mission = mission
            harvest.ward = mission.farm.ward
            harvest.animal = mission.animal 
            harvest.save()
            return redirect('farm:farm_detail',id=i_d)
    else:
        form = Animal_HarvestForm()
    context = {'form':form}
    template = loader.get_template('farming/animal_harvest.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/login/')
def finish_crop_mission(request,id): 
    mission = get_object_or_404(MissionP,id=id)
    i_d = mission.farm.id
    mission.complete = 1
    mission.save()
    return redirect('farm:farm_detail',id=i_d)

@login_required(login_url='/login/')
def finish_animal_mission(request,id): 
    mission = get_object_or_404(MissionA,id=id)
    i_d = mission.farm.id
    mission.complete = 1
    mission.save()
    return redirect('farm:farm_detail',id=i_d)

@login_required(login_url='/login/')
def sell_crop(request,id):  
    harvest = get_object_or_404(Plant_Harvest,id=id)
    i_d = harvest.farm.id
    harvest.sold = 1
    harvest.save()
    return redirect('farm:farm_detail',id=i_d)

@login_required(login_url='/login/')
def sell_animal(request,id):  
    harvest = get_object_or_404(Animal_Harvest,id=id)
    i_d = harvest.farm.id
    harvest.sold = 1
    harvest.save()
    return redirect('farm:farm_detail',id=i_d)