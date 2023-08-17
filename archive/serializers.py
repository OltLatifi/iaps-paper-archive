from rest_framework.serializers import ModelSerializer
from .models import Paper, Author, Category

class author_serializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class category_serializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class paper_serializer(ModelSerializer):
    authors = author_serializer(read_only=True, many=True)
    categories = category_serializer(read_only=True, many=True)

    class Meta:
        model = Paper
        fields = "__all__"