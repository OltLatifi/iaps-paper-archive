from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import paper_serializer, author_serializer, category_serializer
from .models import Paper, Author, Category

class paper_viewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Paper.objects.all()
        serializer = paper_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Paper, id=pk)
        serializer = paper_serializer(queryset)
        return Response(serializer.data)

class author_viewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Author.objects.all()
        serializer = author_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = author_serializer(author)
        response_data = serializer.data

        papers = Paper.objects.filter(authors=author).values("id", "title", "abstract", "publication_date")
        response_data["papers"] = list(papers)

        return Response(response_data)

class category_viewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = category_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = category_serializer(category)
        response_data = serializer.data

        papers = Paper.objects.filter(categories=category).values("id", "title", "abstract", "publication_date")
        response_data["papers"] = list(papers)

        return Response(response_data)