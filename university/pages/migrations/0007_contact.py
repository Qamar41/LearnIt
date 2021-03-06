# Generated by Django 2.2.5 on 2019-12-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_blog_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
