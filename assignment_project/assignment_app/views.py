import csv
import pandas

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import IAP

# Serializer
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = IAP
        fields = "__all__"


# Viewset
class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing IAP Site List.
    """
    queryset = IAP.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]
        excel = pandas.read_excel(file)
        IAP_list = [
                IAP(
                site_id = df['site_id'],
                site_name = df['site_name'],
                country = df['country'],
                order_id = df['order_id'],
                purchase_id = df['purchase_id'],
                csm_name = df['csm_name'],
                serial = df['serial'].lower(),
                ip_address = df['ip_address'],
                model = df['model'],
                macaddr = ':'.join(df['macaddr'][i:i+2] for i in range(0,12,2))
                )
                for i, df in excel.iterrows()
        ]

        IAP.objects.bulk_create(IAP_list)

        return Response("Successfully uploaded the data")
