from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib .auth.models import User


# Team Members
class faculty (models.Model):
    name=models.CharField(max_length=64)
    position=models.CharField(max_length=90)
    image=models.ImageField(upload_to='photos/%Y/%m/%d')
    fb_id=models.URLField()
    twiter_id=models.URLField()
    linkden_id=models.URLField()


    def __str__(self):
        return self.name





# Testimonial


class testimonial(models.Model):
    name=models.CharField(max_length=64)
    image=models.ImageField(upload_to='testimonial/%Y/%m/%d')
    comment=models.TextField(max_length=500)


    def __str__(self):
        return self.name


# about page


class about(models.Model):
    success=models.TextField(max_length=350)
    info=models.TextField(max_length=350)
    danger=models.TextField(max_length=350)
    warning=models.TextField(max_length=350)
    video=models.FileField(upload_to='videos/%Y/%m/%d')
    detail=models.TextField()
    def __str__(self):
        return self.success




# blog

class blog(models.Model):
    title=models.CharField(max_length=190)
    author=models.CharField(max_length=64)
    published_date=models.DateTimeField(default=datetime.now,blank=True)
    image=models.ImageField(upload_to='photos/%Y/%m/%d')
    about_short=models.TextField(max_length=450)
    about_detail=models.TextField()
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

# contact us

class contact(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.name

# for joining our team


class jobform(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    message=models.TextField(max_length=500)
    image=models.ImageField()
    def __str__(self):
        return self.name



class usercreation(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    email=models.EmailField()
    password1=models.CharField(max_length=15)
    # password2=models.CharField(max_length=15)
    checkbox=models.BooleanField(default=True)

    def __str__(self):
        return self.email

# all courses
class home_course(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='courses/%Y/%m/%d')
    Free=models.BooleanField()
    instructor=models.CharField(max_length=64)
    Price=models.IntegerField(blank=True,default=0)
    published_date=models.DateTimeField(datetime.now,default=datetime.now)
    Seats=models.IntegerField(default=12)
    course_outline=models.CharField(max_length=500,default=None,blank=True)
    pre_requirements=models.CharField(max_length=200,default=None,blank=True)
    objectives=models.CharField(max_length=200,default=None,blank=True)

    def __str__(self):
        return self.title


# for lectures of courses

class Lecture(models.Model):
    course=models.ForeignKey(home_course,on_delete=models.CASCADE)
    video_No=models.IntegerField()
    title=models.CharField(max_length=150)
    video=models.FileField(upload_to='course/videos')

    def __str__(self):
        return self.title

    def delete(self, *args,**kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args,**kwargs)






class Comment(models.Model):
    post = models.ForeignKey(home_course,on_delete=models.CASCADE,related_name='comments')
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)