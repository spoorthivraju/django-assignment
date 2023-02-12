from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('site_id', 'site_name', 'country')

class IAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAP
        fields = ('serial', 'ip_address', 'macaddr', 'model')

'''class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'
'''

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('csm_name', 'order_id', 'purchase_id')

class CombinedSerializer(serializers.Serializer):
    class Meta:
        fields = SiteSerializer.Meta.fields + OrderSerializer.Meta.fields + IAPSerializer.Meta.fields