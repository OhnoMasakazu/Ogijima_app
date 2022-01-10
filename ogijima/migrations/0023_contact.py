# Generated by Django 4.0.1 on 2022-01-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0022_auto_20211220_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('content', models.TextField(blank=True, max_length=4000)),
                ('application_file', models.FileField(blank=True, upload_to='media/%Y-%m-%d-%H-%M-%S')),
                ('terms_file', models.FileField(blank=True, upload_to='media/%Y-%m-%d-%H-%M-%S')),
            ],
        ),
    ]
