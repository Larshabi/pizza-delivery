from django.contrib import admin
from .models import Orders
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['size', 'quantity', 'order_status', 'created_at']
    list_filter = ['created_at', 'order_status', 'size']
    
admin.site.register(Orders, OrderAdmin)