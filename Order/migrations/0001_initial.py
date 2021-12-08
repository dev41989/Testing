# Generated by Django 3.2.9 on 2021-12-06 08:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Address_street', models.TextField()),
                ('Address_landmark', models.TextField()),
                ('Address_pincode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('Created_on', models.DateField(default=datetime.datetime.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.product')),
            ],
        ),
    ]
