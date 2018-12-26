from rest_framework import serializers
from .models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('id','title','description','cost','stock','date_created', 'date_modified')
        read_only_fields = ('id','date_created', 'date_modified')

class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ProductImage
        fields = ('id','caption','product','figure','date_created', 'date_modified')
        read_only_fields = ('id','date_created', 'date_modified')