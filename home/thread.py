import threading
from .models import *
from faker import Faker
from asgiref.sync import async_to_sync
import json
import random
from channels.layers import get_channel_layer
fake = Faker()
import random


class CreateStudentsThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total 
        threading.Thread.__init__(self)
        
    def run(self):
        try:
            print('Thread execution started')
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total += 1
                student_obj = Students.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10 , 50)
                )

                data = {'student_name' : student_obj.student_name , 'student_email' : student_obj.student_email , 'address' : student_obj.address}
                async_to_sync(channel_layer.group_send)(
                    'order' ,{
                        'type': 'order_status',
                        'value': json.dumps(
                            {
                            'count' : self.total ,
                            'current' : current_total,
                            'data' : (data),
                            })
                    }
                )
        except Exception as e:
            print(e)
        
        
        