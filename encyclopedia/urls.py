import re
from django.urls import path
from django.core.files.storage import default_storage
from . import views

#filenames = default_storage.listdir("entries")
#E_list = list(sorted(re.sub(r"\.md$", "", filename)
 #               for filename in filenames if filename.endswith(".md")))

urlpatterns = [
    path("wiki/<str:title>", views.Show_Entry, name="title"),
    path("Add/",views.add_arti,name="add"),
    path("Random/", views.random_arti,name="random"),
    path("", views.index, name="index"),
]
