from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import OrderingFilter

# https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering = ["name"]  # Default ordering
    # ordering_fields = ["name"]
    ordering_fields = ["name", "city"]


#  If ordering_fields is not provided then all the fieds get the ordering options

# http://localhost:8000/studentapi/                 -> order by name (default)
# http://localhost:8000/studentapi/?ordering=city       -> order by city
# http://localhost:8000/studentapi/?ordering=-city       -> order by city in reverse order
