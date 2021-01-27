from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from  rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer

# Create your views here.


# class RegisterView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         user_data = serializer.data
#         user_data['status_message'] = "Your account has been created successfully"
#         return Response(user_data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def registration(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user_data = serializer.data
        user_data['status_message'] = "Your account has been created successfully"
        return Response(user_data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

