# Generated by Django 3.2.7 on 2022-01-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0014_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_check',
            name='arrival_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule_check',
            name='departure_time',
            field=models.TimeField(null=True),
        ),
    ]