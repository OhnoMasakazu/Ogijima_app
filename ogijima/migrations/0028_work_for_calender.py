# Generated by Django 4.0.1 on 2022-02-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogijima', '0027_notification_external_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_for_calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('work_start_date', models.DateField()),
                ('work_end_date', models.DateField()),
                ('place', models.FloatField(default=0, help_text='0:全体を利用、1:キッチンのみ利用、2:ギャラリーのみ利用')),
            ],
        ),
    ]