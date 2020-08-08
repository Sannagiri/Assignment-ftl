from django.db import models

# Create your models here.

class User(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones,pytz.all_timezones))

    id = models.CharField(max_length=10,null=False,unique=True,primary_key=True)
    real_name = models.CharField(max_length=50,null=False)
    tz = models.CharField(max_length=32,choices=TIMEZONES,default='UTC')

    def __str__(self):
        return self.id

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='activity_periods')
    start_time = models.CharField(max_length=50, blank=True, null=True)
    end_time = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.id
