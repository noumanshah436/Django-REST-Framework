from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

# Each of the concrete generic views provided is built by combining GenericAPIView, with one or more mixin classes.

# Using concrete view classes, we do not need to define get, post, put, patch or delete methods.


# The following methods are provided by the mixin classes, 
# and provide easy overriding of the object save or deletion behavior.

# perform_create(self, serializer) - Called by CreateModelMixin when saving a new object instance.
# perform_update(self, serializer) - Called by UpdateModelMixin when saving an existing object instance.
# perform_destroy(self, instance) - Called by DestroyModelMixin when deleting an object instance.


# With using the single Views One by One
class StudentList(ListAPIView):
    # Provides a get method handler.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
    # Provides put and patch method handlers.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(DestroyAPIView):
    # Provides a delete method handler.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# With using the combined API Views
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
