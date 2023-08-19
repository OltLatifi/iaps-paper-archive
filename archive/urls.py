from .viewsets import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('papers/', PaperViewSet.as_view({'get': 'list'}), name='paper-list'),
    path('papers/<str:id>/', PaperViewSet.as_view({'get': 'retrieve'}), name='paper-detail'),
]

urlpatterns += router.urls