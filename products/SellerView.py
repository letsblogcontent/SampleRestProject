from rest_framework.views import APIView
from .models import Seller
from rest_framework.response import Response
from .serializers import SellerSerializer
from rest_framework import status


class SellerView(APIView):
    def get(self, request, format=None):
        sellers = Seller.objects.all()
        serialized = SellerSerializer(sellers, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):
        serializer = SellerSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

