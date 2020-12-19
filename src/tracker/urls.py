from django.urls import path
from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('', views.ItemApiView.as_view(), name='items'),
    # path('new_item', views.CreateItemView.as_view(), name='new-item')
]