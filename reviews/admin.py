from django.contrib import admin
from .models import Homenet

# Register your models here.
class HomenetAdmin(admin.ModelAdmin):
    list_display = {'usr_name', 'usrpackage', 'usr_designation', 'user_paid_amount', 'usr_remain_amount', 'usr_net_id', 'usr_conact',  'status_choice' }
admin.site.register(Homenet)