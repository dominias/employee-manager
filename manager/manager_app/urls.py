from django.urls import path
from . import views
from manager_app import views

urlpatterns = [
    path("", views.index, name = "index")
]