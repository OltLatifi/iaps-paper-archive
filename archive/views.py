from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Paper, Author, Category
from django.db.models import Q

@api_view(["GET"])
def search_paper(request):
    search = request.GET.get("search")
    papers = Paper.objects.filter(
        Q(title__contains = search) |
        Q(abstract__contains = search |
        Q(category__name__contains = search) |
        Q(author__name_contains = search))
    )