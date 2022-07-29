from .models import Orders
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default='PENDING')
    class Meta:
        model= Orders
        fields = [
            'size',
            'order_status',
            'quantity',
        ]
        
class OrderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Orders
        fields = [
            'size',
            'order_status',
            'quantity',
            'created_at',
            'updated_at'
        ]
class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields = ['order_status']
        
    