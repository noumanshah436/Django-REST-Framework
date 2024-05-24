Pagination in Django REST Framework (DRF) allows you to manage the amount of data returned by your API endpoints, making it easier to handle large datasets efficiently. DRF provides several pagination styles, such as limit-offset, page number, and cursor pagination.

Let's walk through how to implement pagination using your `Student` model. 

### Step 1: Define the Model

First, ensure you have your `Student` model defined in `models.py`:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
```

### Step 2: Create the Serializer

Create a serializer for the `Student` model in `serializers.py`:

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll']
```

### Step 3: Create the View

Create a view to list the students in `views.py`. Use Django REST Framework's generic views to make this easier. We'll use `ListAPIView` for this example:

```python
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

### Step 4: Configure Pagination

DRF provides several built-in pagination classes. You can configure pagination globally or per view.

#### Global Configuration

To configure pagination globally, update the `settings.py` file:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Adjust the page size as needed
}
```

#### Per-View Configuration

Alternatively, you can configure pagination per view. First, create a pagination class in `pagination.py`:

```python
from rest_framework.pagination import PageNumberPagination

class StudentPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
```

Then, use this pagination class in your view:

```python
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from .pagination import StudentPagination

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
```

### Step 5: Add the URL Configuration

Finally, add the URL pattern for the `StudentListView` in `urls.py`:

```python
from django.urls import path
from .views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
]
```

### Example Requests and Responses

When you make a GET request to `/students/`, you will receive a paginated response. Here are examples of requests and responses:

**Request:**
```
GET /students/
```

**Response:**
```json
{
    "count": 30,  # Total number of student records
    "next": "http://example.com/students/?page=2",
    "previous": null,
    "results": [
        {
            "name": "Alice",
            "roll": 1
        },
        {
            "name": "Bob",
            "roll": 2
        },
        // ... more results up to page_size
    ]
}
```

You can navigate through the pages using the `next` and `previous` links provided in the response.

### PageNumberPagination class attributes

The PageNumberPagination class includes a number of attributes that may be overridden to modify the pagination style.

To set these attributes you should override the PageNumberPagination class, and then enable your custom pagination class as above.

* `django_paginator_class` - The Django Paginator class to use. Default is django.core.paginator.Paginator, which should be fine for most use cases.
* `page_size` - A numeric value indicating the page size. If set, this overrides the PAGE_SIZE setting. Defaults to the same value as the PAGE_SIZE settings key.
* `page_query_param` - A string value indicating the name of the query parameter to use for the pagination control.
* `page_size_query_param` - If set, this is a string value indicating the name of a query parameter that allows the client to set the page size on a per-request basis. Defaults to None, indicating that the client may not control the requested page size.
* `max_page_size` - If set, this is a numeric value indicating the maximum allowable requested page size. This attribute is only valid if page_size_query_param is also set.
* `last_page_strings` - A list or tuple of string values indicating values that may be used with the page_query_param to request the final page in the set. Defaults to ('last',)
* `template` - The name of a template to use when rendering pagination controls in the browsable API. May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely. Defaults to "rest_framework/pagination/numbers.html".

### Customizing Pagination

You can further customize pagination by creating custom pagination classes. For example, if you want to add more details or change the response format:

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomStudentPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'total_students': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'students': data
        })
```

Use `CustomStudentPagination` in your view:

```python
from .pagination import CustomStudentPagination

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomStudentPagination
```

Now the response will include additional details about the pagination:

```json
{
    "total_students": 30,
    "total_pages": 3,
    "current_page": 1,
    "students": [
        {
            "name": "Alice",
            "roll": 1
        },
        {
            "name": "Bob",
            "roll": 2
        },
        // ... more results up to page_size
    ]
}
```

This setup gives you a comprehensive pagination system for your Django REST Framework API.