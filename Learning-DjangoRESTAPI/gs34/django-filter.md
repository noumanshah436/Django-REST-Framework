# DjangoFilterBackend

`DjangoFilterBackend` is part of the `django-filter` library and provides a flexible way to filter querysets in Django REST framework (DRF). Here’s a detailed explanation and examples to illustrate its usage.

### 1. Installation and Setup

**Install `django-filter`:**

```sh
pip install django-filter
```

**Add `'django_filters'` to `INSTALLED_APPS` in `settings.py`:**

```python
INSTALLED_APPS = [
    # other apps
    'django_filters',
]
```

**Configure `DEFAULT_FILTER_BACKENDS` in `settings.py`:**

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

Alternatively, you can specify the filter backend on individual views or viewsets.

### 2. Basic Equality-Based Filtering

**Example Model:**

Suppose you have a `Product` model:

**models.py:**

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
```

**Basic Filtering in a View:**

You can enable simple equality-based filtering by specifying `filterset_fields` in your view.

**views.py:**

```python
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']
```

**Example Requests:**

1. Filter by `category`:

   ```sh
   GET /api/products?category=clothing
   ```

   This will return all products in the "clothing" category.

2. Filter by `in_stock`:

   ```sh
   GET /api/products?in_stock=True
   ```

   This will return all products that are in stock.

3. Combined filters:

   ```sh
   GET /api/products?category=clothing&in_stock=True
   ```

   This will return all products in the "clothing" category that are also in stock.

### 3. Advanced Filtering with `FilterSet`

For more advanced filtering, you can define a `FilterSet` class.

**filters.py:**

```python
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
            'category': ['exact'],
            'in_stock': ['exact'],
        }
```

**Using the `FilterSet` in a View:**

**views.py:**

```python
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
```

**Example Requests:**

1. Filter by name (exact match):

   ```sh
   GET /api/products?name=Jacket
   ```

   This will return all products named "Jacket".

2. Filter by name (case-insensitive containment):

   ```sh
   GET /api/products?name__icontains=jack
   ```

   This will return all products whose names contain "jack", such as "Jacket" or "Hijacking".

3. Filter by category:

   ```sh
   GET /api/products?category=clothing
   ```

4. Filter by in_stock:

   ```sh
   GET /api/products?in_stock=True
   ```

### 4. Setting Up URL Configuration

Ensure your URLs are configured to point to your view.

**urls.py:**

```python
from django.urls import path
from .views import ProductList

urlpatterns = [
    path('api/products/', ProductList.as_view(), name='product-list'),
]
```

### Conclusion

`DjangoFilterBackend` provides a highly customizable way to filter querysets in Django REST framework. You can start with simple equality-based filtering using `filterset_fields`, and for more advanced requirements, define a `FilterSet` class. This allows you to create complex and dynamic query parameters to filter your data efficiently. By following the setup and examples provided, you can integrate powerful filtering capabilities into your DRF APIs.