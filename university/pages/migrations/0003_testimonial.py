# Generated by Django 2.2.5 on 2019-12-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20191213_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='testimonial/%Y/%m/%d')),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
    ]
