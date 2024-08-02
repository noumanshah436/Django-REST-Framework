from rest_framework.routers import DefaultRouter


from products.viewsets import ProductGenericViewSet
# api/v2/products
router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')
urlpatterns = router.urls