from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=277, verbose_name="Student Email")
    age = models.IntegerField()
    gender = models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return str(self.id)