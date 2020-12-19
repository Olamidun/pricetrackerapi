from django.urls import path
from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('', views.items, name='items-list')
]