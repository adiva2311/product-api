from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('api/', ProductListCreate.as_view(), name='product-api'),
    path('api/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-action')
]
