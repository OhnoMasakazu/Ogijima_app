# Generated by Django 3.2.9 on 2021-12-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0006_auto_20211219_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_sample',
            name='sumbnail',
            field=models.CharField(max_length=100),
        ),
    ]