# Generated by Django 4.2.4 on 2023-10-23 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='User',
            new_name='user',
        ),
    ]
