# Generated by Django 2.2.5 on 2019-12-13 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=190)),
                ('author', models.CharField(max_length=64)),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('about_short', models.TextField(max_length=450)),
                ('about_detail', models.TextField()),
            ],
        ),
    ]
