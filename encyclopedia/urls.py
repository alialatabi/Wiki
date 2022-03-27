import re
from django.urls import path
from django.core.files.storage import default_storage
from . import views

#filenames = default_storage.listdir("entries")
#E_list = list(sorted(re.sub(r"\.md$", "", filename)
 #               for filename in filenames if filename.endswith(".md")))

urlpatterns = [
    path("", views.index, name="index"),
    path("css", views.Show_Entry, name="css")
]
