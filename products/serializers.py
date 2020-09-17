from rest_framework import serializers
from .models import Product, Seller, Company, User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'email']


class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'desc', 'company']
        extra_kwargs = {'company': {'required': True}}


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'address', 'email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'city']
