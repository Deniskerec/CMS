from django.contrib import admin
from django.urls import path
from . import views

import CMS

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    #path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="log_out"),
    path("register/", views.register_user, name="register_user"),
]
