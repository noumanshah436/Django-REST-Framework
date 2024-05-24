The `OrderingFilter` in Django REST framework allows you to sort the results of your API views based on one or more model fields. Here's how to implement and use `OrderingFilter` with the `Student` model.

### 1. Model Definition

First, ensure you have the `Student` model defined:

**models.py:**

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    passby = models.CharField(max_length=50)
```

### 2. Adding `OrderingFilter` to a View

You can add the `OrderingFilter` to a view to enable sorting on specified fields.

**views.py:**

```python
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from .models import Student
from .serializers import StudentSerializer

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'roll', 'city', 'passby']
    ordering = ['name']  # Default ordering
```

### 3. URL Configuration

Ensure your URL configuration points to this view.

**urls.py:**

```python
from django.urls import path
from .views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
]
```

### 4. Example Requests

**Basic Usage:**

- **Default ordering by `name`:**

  ```sh
  GET /students/
  ```

  This will return students ordered by their names, as specified by the `ordering` attribute in the view.

- **Order by `roll` in ascending order:**

  ```sh
  GET /students/?ordering=roll
  ```

  This will return students ordered by their roll number in ascending order.

- **Order by `city` in descending order:**

  ```sh
  GET /students/?ordering=-city
  ```

  This will return students ordered by their city in descending order.

- **Order by multiple fields:**

  ```sh
  GET /students/?ordering=city,name
  ```

  This will return students ordered by city first, and then by name within each city.

### 5. Global Configuration (Optional)

You can also set the `OrderingFilter` globally for all views by adding it to the `DEFAULT_FILTER_BACKENDS` in your settings.

**settings.py:**

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',
    ],
}
```

With this global setting, you don't need to specify the filter backend in each view. However, you'll still need to specify `ordering_fields` in each view to define which fields are sortable.

