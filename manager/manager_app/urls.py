from django.urls import path
from . import views
from manager_app import views
from manager_app.forms import UserForm

urlpatterns = [
    path("", views.index, name = "index"),
    path("create_user/", views.create_user, name = "create_user")
]