from django.urls import path
from .views import CreateCart, CreatePayment, CreateSeason
urlpatterns = [
    path('create_payment/', CreatePayment.as_view(), name='create_payment'),
    path('create_cart/', CreateCart.as_view(), name= 'create_cart'),
    path('create_season/', CreateSeason.as_view(), name = 'create_season'),
]
