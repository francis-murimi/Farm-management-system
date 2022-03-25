from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Farmer, Ward
from farm.models import Farm, Crop, Animal
from django.contrib.auth.models import User 

class MissionP(models.Model): 
    MISSION_COMPLETE = (
        (0,"No"),
        (1,"Yes"),
    )
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete= models.CASCADE,null=True,related_name="main_farm")
    crop = models.ForeignKey(Crop, on_delete= models.CASCADE,null=True, related_name="main_crop")
    ward = models.ForeignKey(Ward, on_delete= models.CASCADE,null=True, related_name="p_ward")
    start_time = models.DateField(auto_now_add=True)
    complete = models.IntegerField(choices=MISSION_COMPLETE, default= 0)
    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Crop Planted'
        verbose_name_plural = 'Crops Planted'
    def __str__(self):
        return self.farmer.user.username
    def add_crop_harvest(self): 
        return reverse('farming:crop_harvest',args=[self.id])
    def complete_crop_mission(self): 
        return reverse('farming:finish_crop_mission',args=[self.id])

class MissionA(models.Model): 
    MISSION_COMPLETE = (
        (0,"No"),
        (1,"Yes"),
    )
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete= models.CASCADE,null=True, related_name="main_farming")
    animal = models.ForeignKey(Animal, on_delete= models.CASCADE,null=True, related_name="main_animal")
    ward = models.ForeignKey(Ward, on_delete= models.CASCADE,null=True, related_name="a_ward")
    start_time = models.DateField(auto_now_add=True)
    complete = models.IntegerField(choices=MISSION_COMPLETE, default= 0)
    class Meta:
        ordering = ['start_time']
        verbose_name = 'Animal Kept'
        verbose_name_plural = 'Animals Kept'
    def __str__(self):
        return self.farmer.user.username
    def add_animal_harvest(self): 
        return reverse('farming:animal_harvest',args=[self.id])
    def complete_animal_mission(self): 
        return reverse('farming:finish_animal_mission',args=[self.id])

class Plant_Harvest(models.Model): 
    HARVEST_SOLD = (
        (0,"No"),
        (1,"Yes"),
    )
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete= models.CASCADE,null=True)
    crop = models.ForeignKey(Crop, on_delete= models.CASCADE,null=True)
    mission = models.ForeignKey(MissionP, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=30, help_text="Where the produce can be picked from.")
    ward = models.ForeignKey(Ward, on_delete= models.CASCADE,null=True, related_name="F_ward")
    quantity = models.IntegerField(help_text="Kilograms of the harvest.")
    sold = models.IntegerField(choices=HARVEST_SOLD, default=0)
    created = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
        verbose_name = 'Plant Harvest'
        verbose_name_plural = 'Plant Harvests'
    def __str__(self):
        return self.crop.name
    def sell_crop_harvest(self): 
        return reverse('farming:sell_crop',args=[self.id])

class Animal_Harvest(models.Model): 
    HARVEST_SOLD = (
        (0,"No"),
        (1,"Yes"),
    )
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete= models.CASCADE,null=True)
    animal = models.ForeignKey(Animal, on_delete= models.CASCADE,null=True)
    mission = models.ForeignKey(MissionA, on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=30, help_text="Where the produce can be picked from.")
    ward = models.ForeignKey(Ward, on_delete= models.CASCADE,null=True, related_name="farm_ward")
    quantity = models.IntegerField(help_text="Kilograms of the harvest.")
    sold = models.IntegerField(choices=HARVEST_SOLD, default=0)
    created = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
        verbose_name = 'Animal Harvest'
        verbose_name_plural = 'Animal Harvests'
    def __str__(self):
        return self.animal.name
    def sell_animal_harvest(self): 
        return reverse('farming:sell_animal',args=[self.id])
