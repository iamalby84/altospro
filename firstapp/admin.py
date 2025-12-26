from django.contrib import admin
from firstapp.models import Course, Student
from django.urls import path

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)


