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
    path("record/<int:pk>", views.monthly_record, name="monthly_record"),
    path("delete_record/<int:pk>", views.delete_monthly_record, name="delete_monthly_record"),
    path("add_record/", views.add_monthly_record, name="add_monthly_record"),
    path("update_record/<int:pk>", views.update_monthly_record, name="update_monthly_record"),
]
