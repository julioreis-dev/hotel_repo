# Generated by Django 3.2 on 2022-07-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_alter_reservation_checkin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number_host',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3)], default=1, null=True, verbose_name='Nº of days'),
        ),
    ]
