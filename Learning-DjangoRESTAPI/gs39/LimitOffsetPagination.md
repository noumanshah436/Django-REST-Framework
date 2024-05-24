`LimitOffsetPagination` is a pagination style in Django REST Framework that allows clients to paginate through a large set of results by specifying a limit (number of items per page) and an offset (number of items to skip before starting to return items). This style of pagination is commonly used in APIs to handle large datasets efficiently.

Here's how you can implement `LimitOffsetPagination` in Django REST Framework with an example:

First, you need to configure pagination in your Django REST Framework settings. Add `'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',` to your Django settings file (usually `settings.py`).

```python
# settings.py

REST_FRAMEWORK = {
    ...
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10  # Optional, sets the default page size
    ...
}
```

Next, in your view, you need to define the pagination class and apply it to your queryset.

```python
# views.py

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from myapp.models import YourModel
from myapp.serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    pagination_class = LimitOffsetPagination
```

Now, when you make requests to your API endpoint, you can include `limit` and `offset` query parameters to control pagination.

Example API request:

```
GET /api/yourmodel/?limit=10&offset=20
```

This request will return 10 items starting from the 21st item in the queryset.

Here's how you can implement custom pagination using `LimitOffsetPagination`:

```python
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
```

In this example, we've created a custom pagination class `CustomLimitOffsetPagination` that sets a default limit of 10 items per page and a maximum limit of 100 items. It also overrides the `get_paginated_response` method to customize the response format.

Then, you can use this custom pagination class in your views:

```python
from rest_framework import viewsets
from myapp.models import YourModel
from myapp.serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    pagination_class = CustomLimitOffsetPagination
```

Now, your API responses will follow the custom pagination format specified in `CustomLimitOffsetPagination`.

### Configuration

The LimitOffsetPagination class includes a number of attributes that may be overridden to modify the pagination style.

To set these attributes you should override the LimitOffsetPagination class, and then enable your custom pagination class as above.

* `default_limit` - A numeric value indicating the limit to use if one is not provided by the client in a query parameter. Defaults to the same value as the PAGE_SIZE settings key.
* `limit_query_param` - A string value indicating the name of the "limit" query parameter. Defaults to 'limit'.
* `offset_query_param` - A string value indicating the name of the "offset" query parameter. Defaults to 'offset'.
* `max_limit` - If set this is a numeric value indicating the maximum allowable limit that may be requested by the client. Defaults to None.
* `template` - The name of a template to use when rendering pagination controls in the browsable API. May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely. Defaults to "rest_framework/pagination/numbers.html".