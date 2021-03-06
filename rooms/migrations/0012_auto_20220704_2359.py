# Generated by Django 3.2 on 2022-07-05 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_alter_reservation_client_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotels',
            options={'verbose_name': 'Hotel', 'verbose_name_plural': 'Hotels'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Reservation', 'verbose_name_plural': 'Reservations'},
        ),
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
        migrations.AddField(
            model_name='reservation',
            name='rooms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms'),
        ),
    ]
