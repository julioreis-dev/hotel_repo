# Generated by Django 3.2 on 2022-07-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_rename_adress_hotels_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
