from rest_framework import viewsets
from .models import Paper, Author, Category
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import paper_serializer, author_serializer, category_serializer
from .views_utils import list_objects
from .helpers import (
    search_paper,
    search_category,
    search_author
)

class paper_viewset(viewsets.ViewSet):
    model = Paper
    serializer = paper_serializer

    def list(self, request):
        return list_objects(request, self.model, self.serializer, search_paper)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(self.model, id=pk)
        serializer = self.serializer(queryset)
        return Response(serializer.data)

class author_viewset(viewsets.ViewSet):
    model = Author
    serializer = author_serializer
    
    def list(self, request):
        return list_objects(request, self.model, self.serializer, search_author)

    def retrieve(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = author_serializer(author)
        response_data = serializer.data

        papers = Paper.objects.filter(authors=author).values("id", "title", "abstract", "publication_date")
        response_data["papers"] = list(papers)

        return Response(response_data)

class category_viewset(viewsets.ViewSet):
    model = Category
    serializer = category_serializer

    def list(self, request):
        return list_objects(request, self.model, self.serializer, search_category)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = category_serializer(category)
        response_data = serializer.data

        papers = Paper.objects.filter(categories=category).values("id", "title", "abstract", "publication_date")
        response_data["papers"] = list(papers)

        return Response(response_data)