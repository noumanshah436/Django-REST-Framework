from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get("username")
        if username is None:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("No Such User")
        return (user, None)


# To implement a custom authentication scheme, subclass BaseAuthentication and override the .authenticate(self, request)
#     method. The method should return a two-tuple of (user, auth) if authentication succeeds, or None otherwise.

# In some circumstances instead of returning None, you may want to raise an AuthenticationFailed exception from the
# authenticate() method.

# Typically the approach you should take is:

# If authentication is not attempted, return None. Any other authentication schemes also in use will still be checked.
# If authentication is attempted but fails, raise an AuthenticationFailed exception. An error response will be returned
#       immediately, regardless of any permissions checks, and without checking any other authentication schemes.
