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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Item.objects.filter(user=self.request.user, url=serializer.validated_data['url']).exists():
            return Response({'error': 'This product is already being tracked'})
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)