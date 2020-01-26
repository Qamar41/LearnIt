from django.urls import path
from .import views


urlpatterns=[

    path('',views.index , name='index'),
    path('gallery',views.gallery , name='gallery'),
    # path('about',views.abouts , name='about'),
    # path('blog',views.blogs , name='blog'),
    path('aboutus',views.abouts , name='aboutus'),
    path('contacts',views.contacts , name='contacts'),
    # path('signin',views.login , name='signin'),
    # path('<int:blog_id>',views.blogs , name='blog_details'),
    path('jobform',views.jobforme , name='jobform'),
    path('<int:coursee_id>',views.course , name='course'),
    path('courses',views.courses , name='courses'),


]

