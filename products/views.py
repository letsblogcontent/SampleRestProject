from rest_framework.decorators import api_view
from .models import Product, Seller, Company, User
from rest_framework import status
from .serializers import ProductSerializer, SellerSerializer, CompanySerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from django.http import Http404


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyView(generics.RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SellerView(APIView):
    def get(self, request, format=None):
        sellers = Seller.objects.all()
        serialized = SellerSerializer(sellers, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_list(request, format=None):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, safe=False)


@api_view(['POST'])
def add_product(request, format=None):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product(request, pk, format=None):
    product_obj = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product_obj)
    return Response(serializer.data, status=status.HTTP_200_OK)
