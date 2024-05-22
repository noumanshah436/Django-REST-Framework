from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # For single and specific class
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]


# username: admin
# password: admin
# email: admin@example.com

# *************************************
# authentication: only authorized user can access this api
# permissions: What are the permission have been granted to an authorized user (like update delete permissions)
# *************************************


# permission_classes = [AllowAny]            # Have all permissions (default)
# permission_classes = [IsAuthenticated]     # means that only authenticated user can do anything
# permission_classes = [IsAdminUser]         # For in use only for those User whose IsStaff = True (admins)

# *****************************************
# Global Authentication and Permissions

# we can also define authentication_classes and permission_classes for all the endpoints (globally) of the project,
# by defining the default classed in settings.py file

# For Global Authentication and Permissions - All View classes is effected
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
#     'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
# }

# we can also overrite these global settings in view class by defining authentication_classes and permission_classes
# *****************************************

# We have three type of users:

# 1) normal user (only active flag is true)
# 2) staff user or admin user (staff user flag is true)
# 3) superu user (super user flag is true)

# Only staff user and admin user can login to django admin panel

# *****************************************
