To create a **custom method** in a `ModelViewSet`, you can define a method and expose it as an endpoint by using the `@action` decorator provided by Django REST Framework (DRF). This allows you to handle specific, non-CRUD actions within your viewset.

### **Steps to Create a Custom Method in a `ModelViewSet`**

1. Import the `action` decorator from `rest_framework.decorators`.
2. Define your custom method inside the viewset.
3. Use the `@action` decorator to expose it as an endpoint.
4. Specify the HTTP method(s) the custom action should support (`methods=['GET', 'POST']`).
5. The custom method must return a `Response`.

### **Example**

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Custom method example
    @action(detail=False, methods=['get'])
    def top_students(self, request):
        """
        A custom endpoint to retrieve top-performing students.
        """
        # Example logic: Filter students with roll numbers < 10
        top_students = Student.objects.filter(roll__lt=10)
        serializer = self.get_serializer(top_students, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def update_city(self, request, pk=None):
        """
        A custom endpoint to update the city of a specific student.
        """
        student = self.get_object()  # Get the current student instance
        city = request.data.get('city')
        if city:
            student.city = city
            student.save()
            return Response({'message': 'City updated successfully'})
        return Response({'error': 'City not provided'}, status=400)
```

### **Explanation**

1. **`@action` Parameters**:
   - `detail=True`: This makes the custom method applicable to a single instance (e.g., `/students/<id>/update_city/`).
   - `detail=False`: This makes the custom method applicable to the collection (e.g., `/students/top_students/`).
   - `methods=['get', 'post']`: Specifies the HTTP methods allowed for this action.

2. **Example Endpoints**:
   - `GET /students/top_students/`: Calls the `top_students` method and returns filtered student data.
   - `POST /students/<id>/update_city/`: Calls the `update_city` method and updates the city of the student with the specified ID.

3. **Custom Logic**:
   - In `top_students`, custom query logic is used to filter students.
   - In `update_city`, a single student instance is updated based on data provided in the request.

4. **Accessing Context**:
   - Use `self.get_serializer()` to retrieve a serializer instance.
   - Use `self.get_object()` to get the specific instance being acted upon.

### **Advantages of Custom Methods in ViewSets**
- **Flexibility**: Add non-CRUD operations without creating separate views.
- **Consistency**: Keep all operations related to a resource in the same class.
- **Router Integration**: The `@action` decorator automatically integrates with DRF’s router.

### **Router Configuration**
If you’re using DRF’s `DefaultRouter`, the custom methods are automatically added as endpoints. For example:

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
```

This will generate the following URLs:
- `/students/top_students/` (custom action)
- `/students/<id>/update_city/` (custom action)

### **Conclusion**
Using `@action`, you can easily add custom endpoints to your `ModelViewSet` while maintaining clean and modular code. This is particularly useful for operations that don't fit standard CRUD patterns.



---

### **Other Options with the `@action` Decorator**

The `@action` decorator includes several parameters for customization:

| **Parameter**       | **Description**                                                                                   | **Default**         |
|---------------------|---------------------------------------------------------------------------------------------------|---------------------|
| `detail`            | Specifies whether the action applies to a single object (`True`) or the collection (`False`).     | `False` for collection |
| `methods`           | Specifies the HTTP methods allowed for the action (e.g., `['get', 'post']`).                      | `['get']`           |
| `url_path`          | Customizes the URL path for the action.                                                           | Name of the method  |
| `url_name`          | Customizes the URL name for the action. Useful for reverse lookups.                               | Name of the method  |
| `serializer_class`  | Specifies a custom serializer for the action.                                                    | ViewSet’s serializer |
| `permission_classes`| Specifies custom permissions for the action.                                                     | ViewSet’s permissions |

---

#### **Example Using Other Options**

```python
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Custom serializer, permissions, and URL
    @action(
        detail=True, 
        methods=['post'], 
        url_path='update-grade', 
        url_name='student_update_grade', 
        permission_classes=[IsAuthenticated],
        serializer_class=CustomGradeSerializer
    )
    def update_grade(self, request, pk=None):
        """
        Custom endpoint for updating a student's grade.
        URL: /students/<id>/update-grade/
        """
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Grade updated successfully'})
        return Response(serializer.errors, status=400)
```

- **URL**: `/students/<id>/update-grade/`
- **Custom Serializer**: `CustomGradeSerializer`
- **Custom Permissions**: Only authenticated users can access.

---

### **URL Configuration with DRF Routers**

Custom methods are automatically registered when you use a DRF router:

```python
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
```

For the above `StudentViewSet`:
- `/students/honor-roll/`: List of honor roll students.
- `/students/<id>/update-grade/`: Update a specific student's grade.

---

### **When to Use Each Option**

| **Option**             | **Use Case**                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------|
| `url_path`             | When you need a custom URL structure for your method.                                               |
| `url_name`             | When you need to reference the endpoint in your code using `reverse()`.                             |
| `serializer_class`     | When the action requires a different serializer than the default one used in the viewset.           |
| `permission_classes`   | When the action requires different permissions than the default viewset permissions.                |
| `detail`               | Use `detail=True` for object-specific actions, and `detail=False` for collection-specific actions.  |

---

### **Conclusion**

The `@action` decorator provides flexibility for defining custom methods and endpoints in a `ModelViewSet`. Using options like `url_path`, `methods`, `serializer_class`, and `permission_classes`, you can tailor each action to meet specific requirements while maintaining clean and readable code.