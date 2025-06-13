**`ModelViewSet`**  inherits from a combination of **mixins** (`CreateModelMixin`, `RetrieveModelMixin`, etc.) and **`GenericViewSet`**, and this is where the magic happens.

Here's a detailed breakdown of what's going on:

### What Happens Behind the Scenes

1. **The Mixins**: 
   - Each mixin class, like `CreateModelMixin`, `RetrieveModelMixin`, `UpdateModelMixin`, etc., provides a method to handle a specific type of HTTP request.
     - For example:
       - `CreateModelMixin` provides the `create()` method for handling `POST` requests.
       - `RetrieveModelMixin` provides the `retrieve()` method for handling `GET` requests to retrieve a single object.
       - `UpdateModelMixin` provides the `update()` method for handling `PUT` requests to update an entire object.
       - `DestroyModelMixin` provides the `destroy()` method for handling `DELETE` requests.
       - `ListModelMixin` provides the `list()` method for handling `GET` requests to list all objects.

   These mixins define the **action methods**, but they don't handle the actual HTTP request processing.

2. **`GenericViewSet`**:
   - The **`GenericViewSet`** class is part of DRF's `viewsets` system and provides the **base functionality** for viewsets, but it doesn't implement any of the actual action methods (like `get()` or `post()`) for HTTP requests.
   - What it does is provide a common framework for handling actions and facilitates things like **viewset registration** with a router, **pagination**, and other shared logic.

3. **HTTP Method Dispatch**:
   - When you use a **`ModelViewSet`**, it essentially brings together **both the action methods from the mixins** (like `create()`, `retrieve()`, `update()`, etc.) and the **request dispatching** from `GenericViewSet` that maps HTTP methods to these actions.

   - **The HTTP method handling** (i.e., `GET`, `POST`, `PUT`, `DELETE`) is handled internally by the **`GenericViewSet`** and **the DRF router**. The router automatically routes HTTP requests to the appropriate **action method** that corresponds to the HTTP method, like:
     - `GET /students/` -> Calls `list()` (from `ListModelMixin`)
     - `GET /students/1/` -> Calls `retrieve()` (from `RetrieveModelMixin`)
     - `POST /students/` -> Calls `create()` (from `CreateModelMixin`)
     - `PUT /students/1/` -> Calls `update()` (from `UpdateModelMixin`)
     - `DELETE /students/1/` -> Calls `destroy()` (from `DestroyModelMixin`)

   In other words, you don't need to manually define methods like `get()`, `post()`, `put()`, and `delete()` because **the viewset handles the mapping** of the HTTP methods to the correct action methods automatically.

### How the HTTP Method Mapping Works:
- **When a request hits the API**, DRF checks the HTTP method (`GET`, `POST`, `PUT`, etc.).
- **The viewset** then maps the request to the appropriate **action method** from the mixins:
  - For a `GET` request (to list all students), it calls `list()` from `ListModelMixin`.
  - For a `POST` request (to create a new student), it calls `create()` from `CreateModelMixin`, and so on.
- This is handled through **DRF's routing system**, which automatically directs the requests to the correct actions based on the HTTP method and the viewset's configuration.

### Why No Need to Define `get()`, `post()`, etc.?
- Since **mixins provide the action methods**, and **`GenericViewSet`** helps route the requests to the appropriate mixin method, **you don't need to explicitly define `get()`, `post()`, `put()`, or `delete()`** methods in your viewset class.
- DRF takes care of the **HTTP method dispatching**, and you only need to focus on specifying the logic inside your **action methods** (like `create()`, `list()`, etc.).

### Example:
```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

Even though you don't see `get()`, `post()`, etc., methods here, DRF still handles those requests automatically through its **router** and **mixins**.

---

### Summary:
- **`ModelViewSet`** doesn’t require you to define HTTP methods (`get()`, `post()`, etc.) because it's a combination of **mixins** that implement the actual action methods (like `list()`, `create()`, etc.), and **`GenericViewSet`** provides the logic for dispatching HTTP requests to the correct method.
- The HTTP method handling (mapping `GET` to `list()`, `POST` to `create()`, etc.) is done automatically by DRF's **routing system** and **GenericViewSet**, reducing the need for boilerplate code in your viewset class.