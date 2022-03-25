from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import County, Ward, Farmer
from django.contrib.auth.models import User

class Farm(models.Model): 
    WATER_AVAILABILITY = (
        (0,"All year"),
        (1,"Seasonal"),
        (2,"Hardly"),
    )
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE) 
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    farm_size = models.IntegerField(help_text="Area of Farm in Metres 2")
    water_availability = models.IntegerField(choices=WATER_AVAILABILITY, default=1)
    name = models.CharField(max_length=30 ,help_text= "A name to help you identify your farm" ,null=True ,blank=True)
    def __str__(self):
        return self.name
    def farm_detail_url(self): 
        return reverse('farm:farm_detail',args=[self.id])
    def edit_farm_url(self):
        return reverse('farm:farm_edit',args=[self.id])
    def add_farm_crop(self): 
        return reverse('farming:crop_farming',args=[self.id])
    def add_farm_animal(self): 
        return reverse('farming:animal_farming',args=[self.id])

class Crop(models.Model): 
    CROP_TYPE = (
        (0,"Food crop"),
        (1,"Industrial crop"),
    )
    CROP_PRODUCT = (
        (0,"Cereal"),
        (1,"Vegetative"),
        (2,"Tuber"),
    )
    CROP_GROWTH = (
        (0,"Three months"),
        (1,"Six months"),
        (2,"Annual"),
        (3,"Biannual"),
        (4,"Perennial"),
    )
    name = models.CharField(max_length=40)
    crop_type = models.IntegerField(choices=CROP_TYPE, default=0)
    crop_product = models.IntegerField(choices=CROP_PRODUCT, default=0)
    crop_growth = models.IntegerField(choices=CROP_GROWTH ,default=0)
    def __str__(self):
        return self.name
    def crop_detail_url(self): 
        return reverse('management:crop_detail',args=[self.id])

class Animal(models.Model): 
    ANIMAL_PRODUCT = (
        (0,"Meat"),
        (1,"Milk"),
        (2,"Eggs"),
    )
    ANIMAL_FOOD = (
        (0,"Plants"),
        (1,"Feeds"),
        (2,"Plants and Feeds")
    )
    name = models.CharField(max_length=40)
    animal_product = models.IntegerField(choices=ANIMAL_PRODUCT, help_text="The main product expected from the animal")
    maturity_age = models.IntegerField(help_text="Months for animal to produce intended product")
    animal_feed = models.IntegerField(choices=ANIMAL_FOOD , help_text="The main food the animal feeds on")
    def __str__(self):
        return self.name
    def animal_detail_url(self): 
        return reverse('management:animal_detail',args=[self.id])