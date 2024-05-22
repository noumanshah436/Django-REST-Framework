from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset

# The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, by mixing in the
# behavior of the various mixin classes.

# The actions provided by the ModelViewSet class are :
# list(), retrieve(), create(), update(), partial_update(), and destroy().


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
