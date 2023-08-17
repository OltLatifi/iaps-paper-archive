from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import paper_serializer, author_serializer, category_serializer
from .models import Paper, Author, Category
from rest_framework.pagination import PageNumberPagination
from .helpers import pagination_metadata

paginator = PageNumberPagination()

class paper_viewset(viewsets.ViewSet):
    serializer = paper_serializer

    def list(self, request):
        queryset = Paper.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = self.serializer(result_page, many=True)
        result = pagination_metadata(paginator, serializer.data)
        
        return Response(result)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Paper, id=pk)
        serializer = self.serializer(queryset)
        return Response(serializer.data)

class author_viewset(viewsets.ViewSet):
    serializer = paper_serializer
    
    def list(self, request):
        queryset = Author.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = self.serializer(result_page, many=True)
        result = pagination_metadata(paginator, serializer.data)
        
        return Response(result)

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
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer(result_page, many=True)
        result = pagination_metadata(paginator, serializer.data)
        
        return Response(result)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = category_serializer(category)
        response_data = serializer.data

        papers = Paper.objects.filter(categories=category).values("id", "title", "abstract", "publication_date")
        response_data["papers"] = list(papers)

        return Response(response_data)