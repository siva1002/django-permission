# Generated by Django 3.2.6 on 2022-05-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0002_auto_20220519_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='consumed_time',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='todo',
            name='duetime',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='todo',
            name='remaining_time',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
