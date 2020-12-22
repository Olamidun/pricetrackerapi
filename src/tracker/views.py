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


# class ItemApiView(generics.GenericAPIView):
#     serializer_class = ItemSerializer

#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         user_data['status_message'] = f"Your {user_data['item_title']} has been added"
#         return Response(user_data, status=status.HTTP_201_CREATED)
    


class ItemApiView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)