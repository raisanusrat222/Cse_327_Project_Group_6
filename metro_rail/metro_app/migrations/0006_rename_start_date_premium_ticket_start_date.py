# Generated by Django 3.2.7 on 2021-12-26 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0005_auto_20211226_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premium_ticket',
            old_name='start_Date',
            new_name='start_date',
        ),
    ]