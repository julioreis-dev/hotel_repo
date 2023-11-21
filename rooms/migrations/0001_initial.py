# Generated by Django 3.2 on 2023-11-21 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name Hotel')),
                ('address', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(verbose_name='Nº room')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('active', models.BooleanField(default=True)),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.hotels')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('checkin', models.DateTimeField()),
                ('number_host', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], default=1, null=True, verbose_name='Nº of days')),
                ('client_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rooms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
