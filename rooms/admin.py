from django.contrib import admin
from .models import Hotels, Rooms, Reservation


class HotelsAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class RoomsAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Hotels, HotelsAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Reservation, ReservationAdmin)
