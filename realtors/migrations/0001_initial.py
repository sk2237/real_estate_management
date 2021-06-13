# Generated by Django 3.2.3 on 2021-06-09 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=12)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
            ],
        ),
    ]