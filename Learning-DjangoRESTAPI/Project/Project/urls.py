from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.UserAddShowView.as_view(), name="addandshow"),
    path("<int:id>/", views.UserDeleteView.as_view(), name="deletedata"),
    path("update/<int:id>/", views.UserUpdateView.as_view(), name="updatedata"),
    # urls for django rest api
    path("api/", include("enroll.api.urls")),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
