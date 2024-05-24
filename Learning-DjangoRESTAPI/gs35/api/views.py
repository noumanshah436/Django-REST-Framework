from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter

# https://www.django-rest-framework.org/api-guide/filtering/#searchfilter


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city']
    search_fields = ["name", "city"]
    # search_fields = ['name']
    # search_fields = ['^name']  # search for start with
    # search_fields = ["=name"]  # exact match for search


# http://localhost:8000/studentapi/?search=Phoenix
# http://localhost:8000/studentapi/?search=Bob

# http://localhost:8000/studentapi/?search=o

# http://localhost:8000/studentapi/?search=New York
