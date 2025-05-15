from django.urls import path
from . import views


app_name = "auth_module"

urlpatterns = [
    path('', views.redirect_to_index),
    path('sign-up', views.registration_page, name="registr_page"),
    path('sign-in', views.login_page, name="login_page"),

    path('sign-up/registr', views.registr_user, name="registr_user"),
    path('sign-in/login', views.login_user, name="login_user"),
    ]
