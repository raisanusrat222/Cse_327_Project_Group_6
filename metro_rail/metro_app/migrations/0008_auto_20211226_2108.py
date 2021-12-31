# Generated by Django 3.2.7 on 2021-12-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0007_alter_premium_ticket_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_ticket',
            old_name='name',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='user_ticket',
            old_name='phone_number',
            new_name='source',
        ),
        migrations.RemoveField(
            model_name='user_ticket',
            name='route_id',
        ),
        migrations.AddField(
            model_name='user_ticket',
            name='no_of_tickets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_ticket',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_ticket',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user_ticket',
            name='email_address',
            field=models.EmailField(max_length=500, null=True),
        ),
    ]