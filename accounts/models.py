from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class County(models.Model):  
    name = models.CharField(max_length=20,db_index=True,default="Kirinyaga")
    class Meta:
        ordering = ('name',)
        verbose_name = 'county'
        verbose_name_plural = 'counties'
    def __str__(self):
        return self.name

class Ward(models.Model): 
    name = models.CharField(max_length=20,db_index=True)
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        verbose_name = 'ward'
        verbose_name_plural = 'wards'
    def __str__(self):
        return self.name

class Farmer(models.Model): 
    DISABILITY = (
        (0,"No"),
        (1,"Yes")
        )
    GENDER = (
        (0,"Male"),
        (1,"Female")
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward,on_delete=models.CASCADE)
    national_id = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER, default=0)
    disability = models.IntegerField(choices=DISABILITY, default=0)
    
    def __str__(self):
        return self.user.username