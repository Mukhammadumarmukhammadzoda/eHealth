from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.

class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=255)
    video = models.URLField()
    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Client(AbstractUser):
    user_type = models.IntegerField(choices=(
        (1, "client"),
        (2, "expert")
    ), default=1)
    
    def __str__(self): 
        return self.username

class Expert(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    bio = models.TextField()
    video = models.URLField(null=True,blank=True)
    reyting = models.FloatField(default=0)
    reyting_count = models.IntegerField(default=0)

    def __str__(self):
        return self.client.username

class User(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    type_g = [
        (1, "Erkak"),
        (2,"Ayol")]
    gender = models.IntegerField(choices=type_g)
    register_date = models.DateField()
    week_result = models.IntegerField()
    avarage = models.IntegerField(default=0)
    age = models.IntegerField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    task_sport_can_not = models.ManyToManyField(Sport,)
    days = models.ManyToManyField(Day)
    task_dieta_can_not = models.ManyToManyField(Sport, related_name="NoDieta")
    type_t = [
        (1,"Dieta"),
        (2,"Sport"),
        (3,"All")] 
    task_type = models.IntegerField(choices=type_t)
    
    def __str__(self):
        return self.client.username

class HistoryReyting(models.Model):
    expert = models.ForeignKey(Expert,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    star = models.IntegerField()
    def __str__(self):
        return f"{self.user.client.username} : {str(self.star)} -> {self.expert.client.username}"

class TaskSport(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    activity = models.ForeignKey(Sport, on_delete=models.CASCADE)
    duration = models.IntegerField()


class TaskDieta(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    morning = models.ManyToManyField(Product, related_name='morning_time')
    lunch = models.ManyToManyField(Product, related_name='lunch_time')
    night = models.ManyToManyField(Product)
    limit = models.DateField()

class Advice(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
