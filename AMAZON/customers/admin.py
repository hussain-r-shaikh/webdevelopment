from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    class meta:
        model=Customer

    list_display = ['id','user','mobile','city']


admin.site.register(Customer, CustomerAdmin)