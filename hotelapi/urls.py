from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelsViewSet, ReservationViewSet, RoomsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('hotels', HotelsViewSet, basename='hotels')

urlpatterns = [
    path('', include(router.urls)),
    path('rooms/', RoomsViewSet.as_view(), name='rooms'),
    path('reservations/', ReservationViewSet.as_view(), name='reservations'),
]