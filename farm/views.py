from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import FarmEditForm,FarmAddForm
from .models import Farm, Crop, Animal
from farming.models import MissionA, MissionP, Plant_Harvest, Animal_Harvest
from accounts.models import Farmer
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def farm_list(request):
    username = request.user
    farms = Farm.objects.filter(farmer__user=username) 
    context = {'farms':farms}
    template = loader.get_template('farm/list.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/login/')
def farm_detail(request, id): 
    farm = get_object_or_404(Farm,id=id)
    p_missions = MissionP.objects.filter(farm=farm)
    a_missions = MissionA.objects.filter(farm=farm)
    p_harvests = Plant_Harvest.objects.filter(farm=farm)
    a_harvests = Animal_Harvest.objects.filter(farm=farm)
    contex = {'farm':farm,
                'p_missions':p_missions,
                'a_missions':a_missions,
                'p_harvests':p_harvests,
                'a_harvests':a_harvests,}
    template = loader.get_template('farm/farm_detail.html')
    return HttpResponse(template.render(contex,request))

@login_required(login_url='/login/')
def farm_edit(request,id): 
    farm = get_object_or_404(Farm,id=id)
    if request.method == 'POST':
        form = FarmEditForm(request.POST,request.FILES,instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm:farm_list')
    else:
        form = FarmEditForm(instance=farm)
    contex = {'form':form}
    template = loader.get_template('farm/farm_edit.html')
    return HttpResponse(template.render(contex,request))

@login_required(login_url='/login/')
def add_farm(request): 
    farmer = Farmer.objects.get(user = request.user)
    if request.method == 'POST':
        form =FarmAddForm (request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.farmer = farmer
            farm.save()
            return redirect('farm:farm_list')
    else:
        form = FarmAddForm()
    contex = {'form':form}
    template = loader.get_template('farm/farm_add.html')
    return HttpResponse(template.render(contex,request))