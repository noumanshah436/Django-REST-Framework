from rest_framework.serializers import ModelSerializer
from readers.models import Reader, MarkAsRead
from utility.serializers import RegionSerializer, GenderSerializer
from blogs.serializers import BlogPostSerializer


class ReaderSerializer(ModelSerializer):

    gender = GenderSerializer(read_only=True)
    region = RegionSerializer(read_only=True)

    class Meta:
        model = Reader
        fields = "__all__"


class MarkAsReadSerializer(ModelSerializer):

    blog = BlogPostSerializer(read_only=True)
    reader = ReaderSerializer(read_only=True)

    class Meta:
        model = MarkAsRead
        fields = "__all__"
