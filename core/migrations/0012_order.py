# Generated by Django 4.0.4 on 2022-04-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email adress')),
                ('address', models.CharField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
