from django.urls import path, include
from .views import (
    ItemApiView,
    ItemDetailApiView,
    ItemToggleVisibilityApiView
)

urlpatterns = [
    path('api', ItemApiView.as_view()),
    path('api/<int:id>', ItemDetailApiView.as_view()),
    path('api/<int:id>/toggle-visibility', ItemToggleVisibilityApiView.as_view()),
]