from django.urls import path
from .import views


urlpatterns=[

    path("h", views.index, name="index1"),
    path("loggin", views.login_view, name="loggin"),
    path("loggout", views.logout_view, name="loggout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("signup", views.signup, name="signup"),
    path("change", views.change_password, name="change"),
    path("change", views.change_password, name="change"),

]

