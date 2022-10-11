from django.urls import path, include
from .views import (
    ItemApiView,
    ItemDetailApiView,
    ItemToggleVisibilityApiView,
    ItemFilteredByCategoryApiView
)

urlpatterns = [
    path('api/', ItemApiView.as_view()),
    path(r'^api/(?P<category>\w{0,50})/$', ItemFilteredByCategoryApiView.as_view()),
    path('api/<int:id>', ItemDetailApiView.as_view()),
    path('api/<int:id>/toggle-visibility', ItemToggleVisibilityApiView.as_view()),
]