from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, OwnerViewSet, ToyViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('toys', ToyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]