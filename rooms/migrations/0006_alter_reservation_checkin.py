# Generated by Django 3.2 on 2022-07-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_rooms_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='checkin',
            field=models.DateField(blank=True, null=True),
        ),
    ]