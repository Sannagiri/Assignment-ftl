from django.core.management.base import BaseCommand
from django.utils import timezone
from User.models import *
from django.db import IntegrityError

class Command(BaseCommand):
    help='Adds the User details to database'

    def add_arguments(self,parser):
        parser.add_argument('id', type=str, help='which is unique Id to represnt the User')
        parser.add_argument('real_name', type=str, help='represents the name of the User')
        parser.add_argument('tz',type=str,help='represents the time zone of the User')

    def handle(self,*args,**kwargs):
        emp_id = kwargs['id']
        real_name = kwargs['real_name']
        tz = kwargs['tz']
        try:
            if emp_id is not None:
                if emp_id != "":
                    User.objects.create(id=emp_id, real_name=real_name, tz=tz)
                    self.stdout.write("New User is created for : " + real_name)
                else:
                    self.stdout.write("Employee Id cannot be null")
            else:
                self.stdout.write("Please check the Inputs given")
                
        except IntegrityError as e:
                self.stdout.write("Already User exists with same Employee Id")
        
    
