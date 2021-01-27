from django.urls import path
from accounts import views
from rest_framework.authtoken import views as token_view

app_name = "accounts"

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('login/', token_view.obtain_auth_token)
]

