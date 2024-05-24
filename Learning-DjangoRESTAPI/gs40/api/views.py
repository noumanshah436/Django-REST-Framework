from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypaginations import MyCursorPagination


# https://www.django-rest-framework.org/api-guide/pagination/#cursorpagination
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    pagination_class = MyCursorPagination
