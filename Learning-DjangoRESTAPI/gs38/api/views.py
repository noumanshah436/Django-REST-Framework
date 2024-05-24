from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypaginations import MyPageNumberPagination

# https://www.django-rest-framework.org/api-guide/pagination/#limitoffsetpagination

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    pagination_class = MyPageNumberPagination
