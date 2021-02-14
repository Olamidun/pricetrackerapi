from django.urls import path
from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('', views.ItemApiView.as_view(), name='items'),
    path('<int:pk>', views.SingleItemView.as_view(), name='single-item')
]