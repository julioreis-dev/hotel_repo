# Generated by Django 3.2 on 2022-07-02 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_hotels_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotels',
            old_name='adress',
            new_name='address',
        ),
    ]
