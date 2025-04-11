from django.db import models

# Create your models here.
# Create Company models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),('Non IT', 'Non IT'),
                                                     ('Telecom', 'Telecom')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
                                ('Manager', 'manager'),
                                ('SDE', 'sd'),
                                ('Project Manager', 'pl')))
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    