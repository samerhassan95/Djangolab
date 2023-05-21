from django.db import models
from staff.models import Staff

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100, null=True)
    supervisor = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
