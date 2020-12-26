from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from tracker.models import Item
from tracker.serializers import ItemSerializer

# Create your views here.


class ItemApiView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


























# def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if Item.objects.filter(user=self.request.user, url=serializer.validated_data['url']).exists():
    #         return Response({'error': 'This product is already being tracked'})
    #     url = serializer.validated_data['url']
    #     crawled_data = get_data_from_jumia(url)
    #     serializer.save(user=self.request.user)