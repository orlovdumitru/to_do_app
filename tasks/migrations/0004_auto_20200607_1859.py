# Generated by Django 3.0.7 on 2020-06-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200607_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='finish_date',
            field=models.DateTimeField(blank=True, default=''),
        ),
    ]
