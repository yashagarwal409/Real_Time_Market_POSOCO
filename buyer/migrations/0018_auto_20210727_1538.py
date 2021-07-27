# Generated by Django 3.2.5 on 2021-07-27 10:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0017_timeblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaration',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reserve',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]