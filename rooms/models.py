from django.db import models
from users.models import User
from rooms import DAY_CHOICE


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Hotels(Base):
    name = models.CharField(max_length=200, verbose_name='Name Hotel', unique=True)
    address = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Rooms(Base):
    number = models.IntegerField(verbose_name='Nº room')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Reservation(Base):
    client_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    number_host = models.IntegerField(verbose_name='Nº of days', null=True, blank=True, choices=DAY_CHOICE, default=1)
    rooms = models.ForeignKey(Rooms, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client_user}'

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
