from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    enrolled_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"