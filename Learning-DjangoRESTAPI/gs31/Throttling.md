# Throttling in DRF

Throttling in Django REST Framework (DRF) is a mechanism to control the rate of requests that clients can make to an API. It helps to prevent abuse and ensures that the system remains stable and responsive. DRF provides several built-in throttling classes that you can use to impose various types of rate limits.

### Types of Throttling in Django REST Framework

1. **AnonRateThrottle**
2. **UserRateThrottle**
3. **ScopedRateThrottle**
4. **Custom Throttles**

#### 1. AnonRateThrottle

This throttle is applied to requests from anonymous (unauthenticated) users. It ensures that unauthenticated users cannot overwhelm the API with too many requests. You can configure it globally or per view.

**Configuration:**

In your `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day'  # Adjust the rate limit as needed
    }
}
```

To define throttling for your specific viewsets or endpoints:

```python
class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    throttle_classes = [AnonRateThrottle]
```

How it works:
- It checks if the user is authenticated.
- If not authenticated, it counts the requests made from the user's IP address.
- If the requests exceed the limit, the user receives a `429 Too Many Requests` response.

#### 2. UserRateThrottle

This throttle is applied to requests from authenticated users. It limits the number of requests a user can make within a given time period.

**Configuration:**

In your `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day'  # Adjust the rate limit as needed
    }
}
```

How it works:
- It checks if the user is authenticated.
- If authenticated, it counts the requests made by the user.
- If the requests exceed the limit, the user receives a `429 Too Many Requests` response.

#### 3. ScopedRateThrottle

This throttle allows you to define different rate limits for different parts of your API. It is useful when you have varying levels of API usage across different endpoints.

**Configuration:**

In your `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
        'anon': '100/day',
        'scope1': '10/hour',  # Adjust the rate limit as needed for each scope
        'scope2': '50/day',
    }
}
```

In your views:

```python
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

class MyView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'scope1'
```

How it works:
- You define a `throttle_scope` attribute in your view.
- DRF uses the `throttle_scope` to look up the corresponding rate limit in the `DEFAULT_THROTTLE_RATES`.
- The requests are counted and throttled based on the defined scope.

#### 4. Custom Throttles

You can create custom throttles by subclassing `BaseThrottle` and implementing your own logic. This is useful if you need more granular control over throttling behavior.

**Example:**

```python
from rest_framework.throttling import BaseThrottle

class CustomThrottle(BaseThrottle):
    def allow_request(self, request, view):
        # Implement custom logic to determine if request should be allowed
        return True

    def wait(self):
        # Optionally implement a wait method to indicate how long to wait before making the next request
        return None
```

**Usage:**

In your `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'path.to.CustomThrottle'
    ],
}
```

### Summary

Throttling in Django REST Framework helps to control the rate of requests and ensures fair usage of the API. The main types of throttling are:

- **AnonRateThrottle**: Limits requests from anonymous users.
- **UserRateThrottle**: Limits requests from authenticated users.
- **ScopedRateThrottle**: Allows different rate limits for different parts of the API.
- **Custom Throttles**: Provides flexibility to implement custom throttling logic.

By using these throttling classes, you can protect your API from abuse and ensure it remains available and performant for all users.


<hr>

# inheriting custom throttling classes to change rate limits


You can inherit the built-in throttling classes to create custom throttles with different rates. This approach allows you to define custom throttling behavior while still leveraging the core functionality provided by Django REST Framework.

### Step-by-Step Example with Scopes

#### 1. Define Custom Throttling Classes with Scopes

Add scopes to your custom throttling classes.

```python
# throttles.py

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class CustomAnonRateThrottle(AnonRateThrottle):
    scope = 'custom_anon'  # Define a scope for the anonymous throttle

class CustomUserRateThrottle(UserRateThrottle):
    scope = 'custom_user'  # Define a scope for the user throttle
```

#### 2. Configure Throttling Rates in Settings

In your `settings.py` file, define the rates for each scope.

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'path.to.throttles.CustomAnonRateThrottle',
        'path.to.throttles.CustomUserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'custom_anon': '20/minute',    # Rate for the custom anonymous throttle
        'custom_user': '2000/day',     # Rate for the custom user throttle
    }
}
```

#### 3. Apply Throttling Classes to Views

Use the custom throttling classes in your views.

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from path.to.throttles import CustomAnonRateThrottle, CustomUserRateThrottle

class CustomAnonView(APIView):
    """
    A view that uses the custom throttling class for anonymous users.
    """
    throttle_classes = [CustomAnonRateThrottle]

    def get(self, request, *args, **kwargs):
        return Response({"message": "This view is for anonymous users with a custom rate limit."})

class CustomUserView(APIView):
    """
    A view that uses the custom throttling class for authenticated users.
    """
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomUserRateThrottle]

    def get(self, request, *args, **kwargs):
        return Response({"message": "This view is for authenticated users with a custom rate limit."})
```

### Explanation

1. **Custom Throttling Classes with Scopes:**
   - `CustomAnonRateThrottle` now has a scope `custom_anon`.
   - `CustomUserRateThrottle` now has a scope `custom_user`.

2. **Throttling Rates Configuration:**
   - In the `settings.py` file, the `DEFAULT_THROTTLE_RATES` dictionary includes the rates for the new scopes `custom_anon` and `custom_user`.

3. **CustomAnonView and CustomUserView:**
   - `CustomAnonView` uses the `CustomAnonRateThrottle` class with the rate defined for `custom_anon` scope.
   - `CustomUserView` uses the `CustomUserRateThrottle` class with the rate defined for `custom_user` scope.

### Summary

By defining scopes for your custom throttling classes and setting their rates in the `settings.py` file, you centralize the rate configuration, making it easier to manage and modify as needed. This approach also enhances the maintainability and clarity of your code.