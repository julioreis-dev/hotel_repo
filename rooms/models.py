from django.db import models
from users.models import User
from rooms import DAY_CHOICE


class Base(models.Model):
    """
    Abstract Class used in other classes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        This class makes the class Base be abstract
        """
        abstract = True


class Hotels(Base):
    """
    Class to represent source of information about hotels
    """
    name = models.CharField(max_length=200, verbose_name='Name Hotel', unique=True)
    address = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """
        Class to sort the admin and create a human-readable name for the object
        """
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Rooms(Base):
    """
    Class to represent source of information about rooms
    """
    number = models.IntegerField(verbose_name='Nº room')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        """
        Classe to sort the admin and create a human-readable name for the object
        """
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Reservation(Base):
    """
    Class to represent source of information about reservation
    """
    client_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    number_host = models.IntegerField(verbose_name='Nº of days', null=True, blank=True, choices=DAY_CHOICE, default=1)
    rooms = models.ForeignKey(Rooms, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client_user}'

    class Meta:
        """
        Classe to sort the admin and create a human-readable name for the object
        """
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
