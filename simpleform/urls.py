from .views import CreateAddress
from django.urls import path

urlpatterns = [
    path('form/', CreateAddress.as_view(), name = "address_form")
]
