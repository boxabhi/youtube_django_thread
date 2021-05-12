from django.shortcuts import render
from .models import *
from faker import Faker
fake = Faker()
from .thread import *

import random

def home(request):
        
         
    return render(request , 'index.html' )
