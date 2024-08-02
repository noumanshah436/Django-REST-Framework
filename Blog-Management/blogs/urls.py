
from django.urls import path, include

# from blogs.views import BlogListView
from blogs.views import BlogModelViewset
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register BlogModelViewset with Router
router.register("blogapi", BlogModelViewset, basename="blog")

urlpatterns = [
    path("", include(router.urls)),
    # path('api/blogs/', BlogListView.as_view(), name='view-all'),
]
