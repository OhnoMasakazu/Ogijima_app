# Generated by Django 4.0.1 on 2022-02-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0026_sponsor_banner_link_sponsor_name_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='external_link',
            field=models.BooleanField(default=False, help_text='クリックした際別タブで開くならTrue'),
        ),
    ]
