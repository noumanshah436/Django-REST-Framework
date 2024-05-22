from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":  # request.method == "GET"
            return True  # allow
        return False  # deny


# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions

# Custom permissions:

# To implement a custom permission, override BasePermission and implement either, or both, of the following methods:

# .has_permission(self, request, view)
# .has_object_permission(self, request, view, obj)

# The methods should return True if the request should be granted access, and False otherwise.
