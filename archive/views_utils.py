from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import FieldDoesNotExist
from rest_framework.response import Response
from .helpers import parse_asc_desc, pagination_metadata

def list_objects(request, model, serializer, search_function):
    """
    Lists paginated object, searches objects, and orders them
    """
    paginator = PageNumberPagination()
    search = request.GET.get("search")

    if search:
        queryset = search_function(search)
    else:
        queryset = model.objects.all()

    order_by = request.GET.get("order_by")
    if order_by:
        asc_or_desc = parse_asc_desc(request.GET.get("asc_or_desc", ""))

        try:
            order_by = asc_or_desc + order_by
            queryset = queryset.order_by(order_by)
        except FieldDoesNotExist:
            queryset = queryset.order_by("id")

    result_page = paginator.paginate_queryset(queryset, request)
    serialized_data = serializer(result_page, many=True).data
    result = pagination_metadata(paginator, serialized_data)

    return Response(result)