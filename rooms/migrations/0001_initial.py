# Generated by Django 3.2 on 2022-07-02 16:08

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
                ('adress', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
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
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.hotels')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('checkin', models.DateTimeField(blank=True, null=True)),
                ('number_host', models.IntegerField(blank=True, null=True, verbose_name='Nº of days')),
                ('client_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rooms', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]