from django.contrib import admin

# Register your models here.
from my_app.models import Grades
from my_app.models import Student
admin.register(Grades)
admin.register(Student)
