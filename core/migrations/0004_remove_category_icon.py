# Generated by Django 4.0.4 on 2022-04-14 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]
