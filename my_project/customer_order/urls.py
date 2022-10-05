from django.urls import path, include
from .views import (
    CustomerOrderApiView,
    CustomerOrderDetailApiView
)

urlpatterns = [
    path('api', CustomerOrderApiView.as_view()),
    path('api/<int:id>', CustomerOrderDetailApiView.as_view()),
]