# Generated by Django 3.2.5 on 2021-07-18 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyer', '0005_upreserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClearedReserveUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClearEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('clearedreserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.clearedreserveup')),
            ],
        ),
    ]
