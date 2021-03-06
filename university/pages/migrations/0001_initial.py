# Generated by Django 2.2.5 on 2019-12-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=90)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('fb_id', models.EmailField(max_length=254)),
                ('twiter_id', models.EmailField(max_length=254)),
                ('linkden_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
