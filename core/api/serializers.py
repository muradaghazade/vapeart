from rest_framework import serializers
from core.models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(required=False, many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'images')