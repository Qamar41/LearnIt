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
    # path('info',views.info , name='info'),
    path('infor',views.infor , name='infor'),
    path('edit',views.edit , name='edit'),
    path('update',views.updatee , name='update'),
    path('<update_profile>',views.update_profile , name='update_profile'),
    # path('/edit/<int:id >',views.edit , name='edit'),

]

