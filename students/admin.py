from django.contrib import admin
from .models import Student, School, Book

# Register your models here.
admin.site.register([Student, School, Book])
