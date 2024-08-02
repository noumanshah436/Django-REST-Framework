from rest_framework.serializers import ModelSerializer
from blogs.models import BlogPost
from utility.serializers import DifficultySerializer


class BlogPostSerializer(ModelSerializer):

    difficulty = DifficultySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = "__all__"
