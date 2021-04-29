from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    idDelete = models.BooleanField()
class Student(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    sintro = models.CharField(max_length=20)
    isDelete = models.BooleanField()
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)        # 关联外键

