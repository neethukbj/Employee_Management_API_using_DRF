from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200,blank=True)
    email = models.EmailField()
    department = models.CharField(max_length=50,choices=(
		('HR','hr'),
		('ENGINEER','engineer'),
		('SALES','sales')
		),blank=True,null=True)
    role = models.CharField(max_length=50,choices=(
		('MANAGER','manager'),
		('DEVELOPER',"developer"),
		('ANALYST','analyst')
		),blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
