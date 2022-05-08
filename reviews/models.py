from sys import flags
from django.db import models

# Create your models here.

class Homenet(models.Model):

    status_choice = (('paid','PAID'), ('pending', 'PENDING'), ('disabled/disconnected', 'DISABLED/DISCONNECTED'), ('active', 'ACTIVE'))
    usr_id = models.CharField(primary_key=True, max_length=100)
    usr_name = models.CharField( max_length=100,null= False)
    usr_package = models.CharField( max_length=100, null= False)
    usr_designation = models.CharField( max_length=100, null= False)
    usr_remain_amount = models.CharField( max_length=100, null= False)
    usr_net_id = models.CharField( max_length=100, null= False)
    usr_contact = models.CharField( max_length=100, null = False)
    status_choice = models.CharField( max_length=100, choices = status_choice, default = 'pending')

    def __str__(self):
        return self.usr_name

