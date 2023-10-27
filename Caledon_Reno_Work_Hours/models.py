from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Estimate(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Company = models.CharField(max_length=256)
    Phone = models.IntegerField(default=0)
    City = models.TextField()
    Zip_code = models.CharField(max_length=10)
    Address = models.CharField(max_length=256)
    Blueprints_and_Images = models.ImageField(default='default.jpg', upload_to='Estimates')


class Application(models.Model):
    First_Name = models.TextField()
    Last_Name = models.TextField()
    Email = models.EmailField()
    Phone_Number = models.IntegerField(default=0)
    Resume = models.FileField(default='default.txt', upload_to='Resumes')


class FilledForm(models.Model):
    First_name = models.TextField()
    Last_name = models.TextField()
    Email = models.EmailField()
    Mileage = models.FloatField(default=0)
    Expense_Image = models.ImageField(default='default.jpg', upload_to='Expense_reports', blank=True)
    Expense_Amount = models.FloatField(default=0)
    Client = models.TextField()
    Date = models.DateField()
    Work_type = models.TextField()
    Time_started = models.TimeField()
    Time_ended = models.TimeField()
    Rating = models.IntegerField()
    Notes = models.TextField(default="N/A")
    What_did_you_learn = models.TextField(default="N/A")


class Job(models.Model):
    Key = models.TextField()
    Phase = models.TextField()
    Description = models.TextField()
    Specific_Description = models.TextField()
    Unit_cost = models.FloatField()
    Unit_type = models.TextField()
    GC_Rate_10 = models.FloatField()
    Retail_Rate_40 = models.FloatField()

