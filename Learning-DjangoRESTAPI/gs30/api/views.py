from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# JSON Web Token is a fairly new standard which can be used for token-based authentication. Unlike the built-in
# TokenAuthentication scheme, JWT Authentication doesn't need to use a database to validate a token. A package for JWT
# authentication is djangorestframework-simplejwt which provides some features as well as a pluggable token blacklist app.
