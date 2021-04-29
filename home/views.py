from django.shortcuts import render
from .models import *
from faker import Faker
fake = Faker()
import random
from .thread import CreateStudentsThread 

def home(request):
    count = 100
    CreateStudentsThread(count).start()
    # for i in range(count):
    #     print(i)
    #     Students.objects.create(
    #         student_name = fake.name(),
    #         student_email = fake.email(),
    #         address = fake.address(),
    #         age = random.randint(10 , 50)
    #     )
    
    context = {'result' : 'Your task is started'}
    
    return render(request , 'index.html' , context)
