from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend


# https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filterset_fields = ["name", "city"]


# http://localhost:8000/studentapi/?city=Phoenix
# http://localhost:8000/studentapi/?city=phoenix