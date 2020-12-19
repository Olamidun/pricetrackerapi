from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from tracker.models import Item
from tracker.serializers import ItemSerializer

# Create your views here.

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def items(request):
#     item = Item.objects.filter(user=request.user).all()
#     serializer = ItemSerializer(item, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


class ItemApiView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)