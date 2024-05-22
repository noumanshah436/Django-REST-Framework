from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
)

# https://www.youtube.com/watch?v=CrT2PLynuPk&list=PLbGui_ZYuhijTKyrlu-0g5GcP9nUp_HlN&index=19


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # For single and specific class
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser] # For in use only for those User whose IsStaff = True
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# ************************************

# SessionAuthentication:

# This authentication scheme uses Django's default session backend for authentication. (like we do in django)
# Session authentication is appropriate for AJAX clients that are running in the same session context as your website.

# If successfully authenticated, SessionAuthentication provides the following credentials.

# request.user will be a Django User instance.
# request.auth will be None.

# Unauthenticated responses that are denied permission will result in an HTTP 403 Forbidden response.

# If you're using an AJAX-style API with SessionAuthentication, you'll need to make sure you include a valid CSRF token for any "unsafe" HTTP method calls, such as PUT, PATCH, POST or DELETE requests. See the Django CSRF documentation for more details.

# ************************************

# For session authentication, we need to define url for authentication in urls.py file:

# path("auth/", include("rest_framework.urls", namespace="rest_framework")),

# ************************************

# IsAuthenticatedOrReadOnly permission:

# The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request.
# Requests for unauthenticated users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.

# This permission is suitable if you want to your API to allow read permissions to anonymous users,
# and only allow write permissions to authenticated users.

# ************************************
# DjangoModelPermissions permission:

# This permission class ties into Django's standard `django.contrib.auth` model permissions (permissions like add, delete or update permission we give from admin panel)..

# This permission must only be applied to views that have a .queryset property or get_queryset() method.
# Authorization will only be granted if the user is authenticated and has the relevant model permissions assigned.
# The appropriate model is determined by checking get_queryset().model or queryset.model.

# By default authenticated user have only read permissiosn.

# POST requests require the user to have the add permission on the model.
# PUT and PATCH requests require the user to have the change permission on the model.
# DELETE requests require the user to have the delete permission on the model.

# ************************************
# DjangoModelPermissionsOrAnonReadOnly permission:

# Similar to DjangoModelPermissions, but also allows unauthenticated users to have read-only access to the API.
# ************************************
