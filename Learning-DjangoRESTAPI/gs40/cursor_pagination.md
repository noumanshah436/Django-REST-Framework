# CursorPagination

The cursor-based pagination presents an opaque "cursor" indicator that the client may use to page through the result set. This pagination style only presents forward and reverse controls, and does not allow the client to navigate to arbitrary positions.

`CursorPagination` is another pagination style provided by Django REST Framework that is particularly useful for large datasets. It offers several advantages over `LimitOffsetPagination`, such as better performance for large data sets and more stable pagination when data changes during pagination. `CursorPagination` uses a cursor-based approach, where each page of results includes a cursor that points to the next set of results. This method is more efficient for databases with large tables or dynamic data that frequently changes.

### Key Features of CursorPagination:

1. **Performance**:
   - More efficient for large datasets compared to offset-based pagination because it doesn't require counting all preceding records to find the start point.
   - Uses database indexes effectively, leading to faster queries.

2. **Stability**:
   - More stable when data changes during pagination (e.g., when new records are added or existing ones are deleted) because it relies on unique identifiers (usually timestamps or IDs).

3. **Security**:
   - The cursor is encoded, making it more secure and less prone to manipulation by clients compared to plain offset values.

### Configuration

The CursorPagination class includes a number of attributes that may be overridden to modify the pagination style.

To set these attributes you should override the CursorPagination class, and then enable your custom pagination class as above.

* `page_size` = A numeric value indicating the page size. If set, this overrides the PAGE_SIZE setting. Defaults to the same value as the PAGE_SIZE settings key.
* `cursor_query_param` = A string value indicating the name of the "cursor" query parameter. Defaults to 'cursor'.
* `ordering` = This should be a string, or list of strings, indicating the field against which the cursor based pagination will be applied. For example: ordering = 'slug'. Defaults to -created. This value may also be overridden by using OrderingFilter on the view.
* `template` = The name of a template to use when rendering pagination controls in the browsable API. May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely. Defaults to "rest_framework/pagination/previous_and_next.html".

### Example Implementation:

Here's how you can implement `CursorPagination` in Django REST Framework:

#### Step 1: Define the Pagination Class

```python
from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    page_size = 10  # Number of items per page
    ordering = '-created'  # Order by created field in descending order
    cursor_query_param = 'cursor'
```

#### Step 2: Apply the Pagination Class to a View

```python
from rest_framework import viewsets
from myapp.models import YourModel
from myapp.serializers import YourModelSerializer

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all().order_by('-created')
    serializer_class = YourModelSerializer
    pagination_class = CustomCursorPagination
```

#### Example API Request:

- To get the first page of results: 
  ```
  GET /api/yourmodel/
  ```

- To get the next page using the cursor provided in the previous response:
  ```
  GET /api/yourmodel/?cursor=<encoded_cursor>
  ```

### Advantages and Use Cases:

- **Real-time Data**: Ideal for applications where data changes frequently, ensuring that clients don't miss or duplicate records.
- **Improved Performance**: Reduces the overhead associated with offset-based pagination, particularly for deep pagination requests.
- **Efficiency**: More efficient for large datasets as it avoids the performance issues of large offsets.
- **Consistency**: Reduces the likelihood of items being missed or duplicated when records are inserted or deleted during pagination.

### Limitations

- **Complexity**: Slightly more complex to implement and understand compared to offset-based pagination.
- **Ordering Requirement**: Requires a consistent ordering field that uniquely identifies records.


### Summary:

`CursorPagination` is a powerful and efficient way to handle pagination in APIs, especially suited for large datasets and dynamic data environments. By configuring attributes such as `ordering`, `page_size`, and `cursor_query_param`, you can customize the pagination behavior to meet your specific requirements.