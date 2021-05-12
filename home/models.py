from django.db import models

# Create your models here.



class Informations(models.Model):
    text = models.CharField(max_length=100)
    json_data = models.TextField(default="{}")

class Images(models.Model):
    image = models.ImageField(upload_to='images')



class Students(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.student_name
    