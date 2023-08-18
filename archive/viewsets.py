from rest_framework import viewsets
from rest_framework import filters
from rest_framework import pagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Paper, Author, Category
from .serializers import paper_serializer, author_serializer, category_serializer
from rest_framework.pagination import PageNumberPagination

class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = paper_serializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'abstract', 'authors__name', 'categories__name']
    ordering_fields = ['title', 'abstract', 'authors__name', 'categories__name']

    def retrieve(self, request, pk=None):
        paper = get_object_or_404(Paper, id=pk)
        serializer = self.serializer_class(paper)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = author_serializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'paper__title', 'paper__abstract', 'paper__categories__name']
    ordering_fields = ['name']

    def retrieve(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = self.serializer_class(author)
        papers = author.paper_set.values("id", "title", "abstract", "publication_date")
        response_data = serializer.data
        response_data["papers"] = list(papers)
        return Response(response_data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = category_serializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'paper__title', 'paper__abstract', 'paper__authors__name']
    ordering_fields = ['name']

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = self.serializer_class(category)
        papers = category.paper_set.values("id", "title", "abstract", "publication_date")
        response_data = serializer.data
        response_data["papers"] = list(papers)
        return Response(response_data)
