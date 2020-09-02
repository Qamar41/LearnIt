from .import views

from django.urls import path
urlpatterns=[
    path('enroll',views.enrollment , name='enroll'),
    path('dashbord',views.dashboard , name='dashboard'),

]