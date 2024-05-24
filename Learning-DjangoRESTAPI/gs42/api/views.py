from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
# Create your views here.
class StudentModelviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# python manage.py shell

# from api.serializers import StudentSerializer
# serializer = StudentSerializer()
# print(repr(serializer))

# output:

# StudentSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     url = HyperlinkedIdentityField(view_name='student-detail')
#     name = CharField(max_length=50)
#     roll = IntegerField(max_value=9223372036854775807, min_value=-9223372036854775808)
#     city = CharField(max_length=50)