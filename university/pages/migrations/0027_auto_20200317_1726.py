# Generated by Django 2.0.1 on 2020-03-17 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
