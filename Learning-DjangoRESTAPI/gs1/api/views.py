import json
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Serialization:
# Serialization is the process of converting Python objects (e.g., model instances, dictionaries) into a format like JSON
# or XML that can be easily transmitted over the network or stored.


# For Single student data
# http://localhost:8000/stuinfo/1
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)  # convert to python dict

    # print(serializer.data)
    # {'id': 1, 'name': 'FirstStudent', 'roll': 1, 'city': 'Manchester'}

    # print(type(serializer.data))
    # <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")

    return JsonResponse(serializer.data)


# FOr all Student data
# http://localhost:8000/stuinfo
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data, safe=False)
