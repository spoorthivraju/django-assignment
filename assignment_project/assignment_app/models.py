from django.db import models
from django.conf import settings

class IAP(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=50,null=False)
    country = models.CharField(max_length=50,null=False)
    order_id = models.IntegerField(null=False)
    purchase_id = models.IntegerField(null=False)
    csm_name = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    macaddr = models.CharField(max_length=30)