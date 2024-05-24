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


# To implement a custom authentication scheme, subclass BaseAuthentication and override the .authenticate(self, request)
#     method. The method should return a two-tuple of (user, auth) if authentication succeeds, or None otherwise.

# In some circumstances instead of returning None, you may want to raise an AuthenticationFailed exception from the .
# authenticate() method.

# Typically the approach you should take is:

# If authentication is not attempted, return None. Any other authentication schemes also in use will still be checked.
# If authentication is attempted but fails, raise an AuthenticationFailed exception. An error response will be returned
#       immediately, regardless of any permissions checks, and without checking any other authentication schemes.
