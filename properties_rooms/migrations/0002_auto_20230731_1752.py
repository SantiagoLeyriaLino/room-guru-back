# Generated by Django 3.2.4 on 2023-07-31 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='properties', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rooms', to='properties_rooms.property'),
        ),
    ]
