from django.db import models

# Create your models here.
class employee(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    employeeid=models.CharField(max_length=40)
    mobile=models.BigIntegerField()
    dateofbirth=models.DateField()
    experience=models.IntegerField()
    salary=models.IntegerField()
