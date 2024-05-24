from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import JackrateThrottle


# https://www.django-rest-framework.org/api-guide/throttling/


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, JackrateThrottle]


# Throttling is similar to permissions, in that it determines if a request should be authorized. Throttles indicate a temporary
# state, and are used to control the rate of requests that clients can make to an API.

# We can set global settings or chANGE DEFAULT settings in settings.py file
