from django.contrib import admin
from django.utils.html import format_html

from .models import *

# Register your models here.
#from django.contrib import admin
#from .models import Truck, Driver, Material, Customer, Order, Invoice, Payment

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'reg_number', 'capacity')
    list_filter = ('year',)
    search_fields = ('name', 'reg_number')


@admin.register(Contact_Detail)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_details', 'Role', 'address')
    search_fields = ('name', 'Role')
    list_filter = ('Role',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_details', 'billing_information', 'information')
    search_fields = ('name', 'contact_details', )
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'truck','delivery_location', 'delivery_date', 'material', 'quantity', 'price', 'cost_price','paymentdone', 'amount_paid', 'amount_pending')
    list_filter = ('customer','truck', 'material', 'delivery_date', 'paymentdone')
    search_fields = ('customer__name', 'truck__name', 'delivery_location', 'material__name')


@admin.register(Agreement)

class AgreementAdmin(admin.ModelAdmin):
    list_display = ('customer','topic', 'agreement_file_display', 'created_at')
    search_fields = ('created_at', 'customer', 'topic')
    
    def agreement_file_display(self, obj):
      if obj.agreement_file:
        lst = obj.agreement_file.name.split('/')
        return format_html('<a href="{}">{}</a>', obj.agreement_file.url, lst[1])
      else:
        return "No file"
    agreement_file_display.short_description = 'Agreement File'
