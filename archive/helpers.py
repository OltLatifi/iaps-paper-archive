def pagination_metadata(paginator, results):
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