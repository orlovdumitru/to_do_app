# Generated by Django 3.0.7 on 2020-06-07 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_todo_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='title',
        ),
    ]
