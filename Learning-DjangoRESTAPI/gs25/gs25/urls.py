from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register("studentapi", views.StudentModelViewset, basename="student")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    # this was for login, using username and password
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    # this is the endpoint for generating token
    path("gettoken/", obtain_auth_token),
]
