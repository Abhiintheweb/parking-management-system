from rest_framework import routers
from .views import VehicleViewSet

router = routers.SimpleRouter()

router.register(r'v1/vehicle', VehicleViewSet)

urlpatterns = []

urlpatterns += router.urls
