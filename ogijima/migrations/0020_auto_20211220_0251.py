# Generated by Django 3.2.9 on 2021-12-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0019_auto_20211220_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
