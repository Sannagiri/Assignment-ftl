from django.core.management.base import BaseCommand
from django.utils import timezone
from User.models import *
from django.db import IntegrityError
import datetime

class Command(BaseCommand):
    help='Adds the activity periods for User'

    def add_arguments(self,parser):
        parser.add_argument('Employee_Id', type=str, help='Foreign key to which the activity periods to be assigned')
        parser.add_argument('Start_Time', type=str, help='represnts the date and time of activity')
        parser.add_argument('End_Time', type=str, help='represnts the date and time of activity')

    def handle(self,*args,**kwargs):
        emp_id = kwargs['Employee_Id']
        start_time = kwargs['Start_Time']
        end_time = kwargs['End_Time']

        e = User.objects.filter(Employee_Id=emp_id)
        try:
            if e is not None:
                ActivityPeriod.objects.create(user=User.objects.get(Employee_Id=emp_id), Start_Time=start_time, End_Time=end_time)
                self.stdout.write("Created successfully")
            else:
                self.stdout.write("Employee Id cannot be null")

        except User.DoesNotExist:
            self.stdout.write("Employee Id does not exists")