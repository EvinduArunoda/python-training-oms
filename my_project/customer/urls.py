from django.urls import path, include
from .views import (
    CustomerApiView,
    CustomerDetailApiView
)

urlpatterns = [
    path('api', CustomerApiView.as_view()),
    path('api/<int:id>', CustomerDetailApiView.as_view()),
]