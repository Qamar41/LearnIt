from django.db import models
from datetime import datetime
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Personal_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name=models.CharField(max_length=64,default='')
    Cnic=models.CharField(max_length=13,default='')
    description=models.CharField(max_length=400,default='')
    date_of_birth=(models.DateTimeField(datetime.now))
    whattsapp=models.CharField(max_length=25,default='')
    phone=models.IntegerField(max_length=25,default='')
    address=models.CharField(max_length=200, default='')
    profile_pic=models.ImageField(upload_to='proflie/profile_pic')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Personal_info.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.personal_info.save()