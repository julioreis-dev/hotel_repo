from django.urls import path
from rooms.views import HomepageView, HotelsListView, HotelDetailView, ReservationCreateView, MyreservationListView
from rooms.views import RoomsUpdateView

app_name = 'rooms'

urlpatterns = [
    path('', HomepageView.as_view(), name='home_rooms'),
    path('hotels/', HotelsListView.as_view(), name='list_hotels'),
    path('hotel/rooms/<int:pk>/', HotelDetailView.as_view(), name='list_rooms'),
    path('hotel/rooms/reserve/<int:pk>/', ReservationCreateView.as_view(), name='reservation_rooms'),
    path('hotel/reservations/<int:pk>/', MyreservationListView.as_view(), name='my_reservations'),
    path('hotel/update/<int:pk>/', RoomsUpdateView.as_view(), name='update_reservation'),
]
