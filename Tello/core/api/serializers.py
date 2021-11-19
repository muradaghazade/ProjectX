from rest_framework import serializers
from core.models import ProductVersion

class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        fields = ('id','color', 'storage', 'quantity', 'product')