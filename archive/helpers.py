from .models import Paper, Author, Category
from django.db.models import Q

def pagination_metadata(paginator, results: dict):
    """
    Adds pagination metadata to the result
    """
    return {
            'count': paginator.page.paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'page_size': paginator.page_size,
            'current_page': paginator.page.number,
            'last_page': paginator.page.paginator.num_pages,
            'results': results
        }

def search_paper(search: str):
    """
    Filters papers based on title, abstract, author's name and categorie's name
    """
    papers = Paper.objects.filter(
        Q(title__contains=search) |
        Q(abstract__contains=search) |
        Q(categories__name__contains=search) |
        Q(authors__name__contains=search)
    )

    return papers

def search_author(search: str):
    """
    Filters authors based on name, their paper's abstract, thier paper's abstract
    and their paper's categorie's name
    """
    authors = Author.objects.filter(
        Q(name__contains=search) |
        Q(paper__title__contains=search) |
        Q(paper__abstract__contains=search) |
        Q(paper__categories__name__contains=search)
    )

    return authors

def search_category(search: str):
    """
    Filters categories based on name, their paper's abstract, thier paper's abstract
    and their paper's categorie's name
    """
    categories = Category.objects.filter(
        Q(name__contains=search) |
        Q(paper__title__contains=search) |
        Q(paper__abstract__contains=search) |
        Q(paper__categories__name__contains=search)
    )

    return categories
