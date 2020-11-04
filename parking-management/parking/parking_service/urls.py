from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

from .views import IndexView, ParkingViewSet, ParkingInteractionViewSet, ListParking

router = routers.SimpleRouter()
router.register(r'v1/parking', ParkingViewSet)
router.register(r'v1/parking-interaction', ParkingInteractionViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('v1/exit/<int:interaction_id>', ListParking.as_view(), name='index')
]

urlpatterns += router.urls
