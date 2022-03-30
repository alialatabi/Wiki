import re
from django.urls import path
from django.core.files.storage import default_storage
from . import views


urlpatterns = [
    path("<str:title>/Edit/",views.edit,name="edit"),
    path("wiki/<str:title>/", views.Show_Entry, name="show"),
    path("Add/",views.add_arti,name="add"),
    path("Random/", views.random_arti,name="random"),
    path("", views.index, name="index"),
]
