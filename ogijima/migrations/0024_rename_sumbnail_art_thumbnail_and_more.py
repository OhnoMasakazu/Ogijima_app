# Generated by Django 4.0.1 on 2022-01-20 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0023_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='restaurant_sample',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='sumbnail',
            new_name='thumbnail',
        ),
    ]
