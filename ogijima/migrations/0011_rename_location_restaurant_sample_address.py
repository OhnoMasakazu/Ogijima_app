# Generated by Django 3.2.9 on 2021-12-19 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0010_restaurant_sample_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant_sample',
            old_name='location',
            new_name='address',
        ),
    ]