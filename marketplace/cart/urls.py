from django.urls import path
from .views import AddToCartView, CartView

urlpatterns = [
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('', CartView.as_view(), name='cart-view'),
]
