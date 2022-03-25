from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm, FarmerProfileForm, LoginForm
from .models import Farmer
from django.contrib.auth.models import User


# The function that shows the home page
def home(request):
    if request.user.is_authenticated: 
        username = request.user.username
    else:
        username = 'not logged in'
    context = {'username':username,}
    template = loader.get_template('accounts/home.html')
    return HttpResponse(template.render(context,request))

# The function that allows registration of farmers
def farmer_register(request):
    template = loader.get_template('accounts/farmer_register.html')
    if request.method == 'POST':
        form =ExtendedUserCreationForm(request.POST)
        profile_form = FarmerProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username,password=password)
            login(request,user)
            return HttpResponse('Successful registration')
    else:
        form = ExtendedUserCreationForm()
        profile_form = FarmerProfileForm()
    
    context = {'form':form,'profile_form':profile_form}
    return HttpResponse(template.render(context,request))

#The function that allows any registered user to log in.
def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect ('accounts:home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
    form = LoginForm()
    template = loader.get_template('accounts/login.html')
    context = {'form':form}
    return HttpResponse(template.render(context,request))


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('accounts:home')

def check_user(request): 
    username = request.user
    farmer_count = Farmer.objects.filter(user=username).count()
    if farmer_count < 1: 
        return redirect('farm:farm_list')
    else: 
        return redirect('accounts:home')