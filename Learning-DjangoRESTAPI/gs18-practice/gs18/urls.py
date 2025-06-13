from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('/', health_check, name='health'),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
