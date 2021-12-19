# Generated by Django 3.2.9 on 2021-12-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0011_rename_location_restaurant_sample_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant_sample',
            old_name='maplink',
            new_name='apple_maplink',
        ),
        migrations.AddField(
            model_name='restaurant_sample',
            name='google_maplink',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
