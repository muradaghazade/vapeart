# Generated by Django 4.0.4 on 2022-04-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Shipping Text',
                'verbose_name_plural': 'Shipping Texts',
            },
        ),
    ]
