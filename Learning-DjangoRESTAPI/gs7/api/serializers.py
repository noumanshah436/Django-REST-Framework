from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Student


# Model based Serializers
class StudentSerializer(serializers.ModelSerializer):
    # For aplying such arg to a specific field
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ["name", "roll", "city"]
        # For multiple fields
        # read_only_fields = ['name', 'roll']

        extra_kwargs = {"name": {"read_only": True}}


# If we want to pass arguments to specific field, there are several ways:

# 1) specify that field in serializer
#     name = serializers.CharField(read_only=True)

# 2) Pass options as
#    read_only_fields = ['name', 'roll']

# 3) Specify extra argument in extra_kwargs as dictionary for each field
