# Generated by Django 3.2.5 on 2021-07-18 18:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyer', '0011_auto_20210718_2335'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClearEntity',
            new_name='ClearEntityUp',
        ),
        migrations.AlterField(
            model_name='clearedreserveup',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 18, 13, 3, 732621, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ClearEntityDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('clearedreserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.clearedreserveup')),
            ],
        ),
        migrations.CreateModel(
            name='ClearedReserveDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_block', models.CharField(default='NoTime', max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 7, 18, 18, 13, 3, 791631, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
