from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from utility.models import Difficulty, Gender, Region


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class DifficultySerializer(ModelSerializer):

    class Meta:
        model = Difficulty
        fields = "__all__"


class GenderSerializer(ModelSerializer):

    class Meta:
        model = Gender
        fields = "__all__"


class RegionSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = "__all__"
