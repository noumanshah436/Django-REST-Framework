from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register("studentapi", views.StudentViewSet, basename="student")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]


# Here is the list of URLs and their corresponding methods created for this router:

# 1. **`GET /studentapi/`** - `list()`
# 2. **`POST /studentapi/`** - `create()`
# 3. **`GET /studentapi/<pk>/`** - `retrieve()`
# 4. **`PUT /studentapi/<pk>/`** - `update()`
# 5. **`PATCH /studentapi/<pk>/`** - `partial_update()`
# 6. **`DELETE /studentapi/<pk>/`** - `destroy()`