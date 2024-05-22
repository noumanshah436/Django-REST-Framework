from rest_framework import serializers
from .models import Student


# Validators Concepts
def starts_with_r(value):
    if value[0].lower() != "r":
        raise serializers.ValidationError("Name should Start with R")


def starts_with_capital_letter(value):
    if not value[0].isupper():
        raise serializers.ValidationError("Name should start with a capital letter")


class StudentSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=100)
    name = serializers.CharField(validators=[starts_with_capital_letter])
    # name = serializers.CharField(max_length=100, validators=[starts_with_r])
    # name = serializers.CharField(validators=[starts_with_r, starts_with_capital_letter])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance

    # Field level validation
    def validate_roll(self, value):
        print("validate_roll")
        if value >= 200:
            raise serializers.ValidationError("Seats Full")
        return value

    # Object level Validation
    def validate(self, data):
        print("validate")
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower() == "nouman" and ct.lower() != "lahore":
            raise serializers.ValidationError("City must be Lahore for Nouman")
        return data


# `validate` method will not be called if there is any field level validation error occured

# custom class validator:
# https://stackoverflow.com/questions/31278418/django-rest-framework-custom-fields-validation