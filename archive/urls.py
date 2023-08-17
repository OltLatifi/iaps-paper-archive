from .viewsets import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'authors', author_viewset, basename='author')
router.register(r'categories', category_viewset, basename='category')

urlpatterns = [
    path('papers/', paper_viewset.as_view({'get': 'list'}), name='paper-list'),
    path('papers/<str:pk>/', paper_viewset.as_view({'get': 'retrieve'}), name='paper-detail'),
]

urlpatterns += router.urls