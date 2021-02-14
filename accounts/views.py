from django.shortcuts import get_object_or_404
from  rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer

# Create your views here.

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


# class ProfileView(generics.RetrieveUpdateAPIView):
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated, )

#     def get_queryset(self):
#         qs = Profile.objects.all()
#         logged_in_user_profile = qs.filter(user=self.request.user)
#         return logged_in_user_profile

#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = get_object_or_404(queryset, user=self.request.user)
#         return obj
         

