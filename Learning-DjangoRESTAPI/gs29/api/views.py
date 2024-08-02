from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .customauth import CustomAuthentication


# https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
