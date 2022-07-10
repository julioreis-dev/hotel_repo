from django.contrib import admin
from .models import Hotels, Rooms, Reservation


class HotelsAdmin(admin.ModelAdmin):
    """
    Class responsible to custom Hotel admin enviroment
    """
    list_display = ('name', 'address', 'active')
    search_fields = ('name',)
    list_filter = ('name',)
    readonly_fields = ("created_at", "updated_at")


class RoomsAdmin(admin.ModelAdmin):
    """
    Class responsible to custom Rooms admin enviroment
    """
    list_display = ('number', 'hotels', 'price', 'active')
    search_fields = ('number', 'hotels__name')
    list_filter = ('number',)
    readonly_fields = ("created_at", "updated_at")


class ReservationAdmin(admin.ModelAdmin):
    """
    Class responsible to custom Reservation admin enviroment
    """
    list_display = ('client_user', 'rooms', 'checkin', 'number_host')
    search_fields = ('client_user__username',)
    list_filter = ('client_user',)
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Hotels, HotelsAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Reservation, ReservationAdmin)
