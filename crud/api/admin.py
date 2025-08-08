from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student  # model import karo

# Simple register


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']
