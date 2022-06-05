from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PledgeViewSet

router = DefaultRouter()
router.register("api", PledgeViewSet)

urlpatterns = [path("", include(router.urls))]
