# Generated by Django 2.0.1 on 2020-03-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_auto_20200317_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_course',
            name='instructor',
            field=models.CharField(max_length=64),
        ),
    ]
