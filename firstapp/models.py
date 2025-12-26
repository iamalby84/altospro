from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()
    join_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
