# Generated by Django 3.2.9 on 2021-11-16 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookstore', '0004_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api_author',
            old_name='added_by_id',
            new_name='added_by',
        ),
    ]
