from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypaginations import MyLimitOffsetPagination


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    pagination_class = MyLimitOffsetPagination


# http://localhost:8000/studentapi/?limit=10&offset=20

# this ill return 10 items starting from the 21st item in the queryset.

# limit = number of records fetched
# offset = starting point
