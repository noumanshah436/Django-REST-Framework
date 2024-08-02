# GenericAPIView and Model Mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

# https://www.django-rest-framework.org/api-guide/generic-views/

# GenericAPIView:

# This class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.
# Each of the concrete generic views provided is built by combining GenericAPIView, with one or more mixin classes.

# more on GenericAPIView

# https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ViewSet

# Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet.

# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and
#   instead provides actions such as .list() and .create().

# The method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using the .as_view() method.

# Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.
