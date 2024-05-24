from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.throttling import ScopedRateThrottle

# we are using gs15 code here

# Here we are defining seperate throttling for different endpoints


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "viewstu"


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "modifystu"


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "viewstu"


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "modifystu"


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "modifystu"
