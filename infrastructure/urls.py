from django.urls import path
from .views import CreateOrderView

urlpatterns = [
    path('api/orders/create/', CreateOrderView.as_view(), name='create_order')
]
