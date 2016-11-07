from django.db import models

# Create your models here.
class Center(models.Model):
        name=models.CharField(max_length=50,default="unnamed center")
        state=models.CharField(max_length=2,default="PA")
        acceptsrodents=models.BooleanField(default=False)
        acceptsdogscats=models.BooleanField(default=False)
        acceptsprimates=models.BooleanField(default=False)
        acceptsbirds=models.BooleanField(default=False)
        phone=models.CharField(max_length=12,default='Unknown')
        desc=models.TextField(default="No description provided")
        site=models.CharField(max_length=30,default="no website")
        siteurl=models.CharField(max_length=70,default="#")
        def __str__(self):
                return self.name
class Animal(models.Model):
        gender=models.PositiveSmallIntegerField(default=2)#0=boy 1=girl 2=unknown
        species=models.PositiveSmallIntegerField(default=4)#rodent,dog/cat,primate,other
        domestic=models.BooleanField(default=False)
        def __str__(self):
                return ['','Domestic '][self.domestic]+['Male ','Female ',''][self.gender]+['rodent','dog/cat','primate', 'other'][self.species]
