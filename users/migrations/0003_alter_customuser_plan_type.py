# Generated by Django 3.2.4 on 2023-08-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='plan_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
