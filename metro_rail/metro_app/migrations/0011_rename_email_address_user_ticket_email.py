# Generated by Django 3.2.7 on 2021-12-26 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0010_auto_20211226_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_ticket',
            old_name='email_address',
            new_name='email',
        ),
    ]