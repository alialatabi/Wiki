from turtle import tilt
from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", context={
        "entries": util.list_entries()
    })

def Show_Entry(request,title):

    article = markdown2.markdown(util.get_entry(title))

    return render(request,"encyclopedia/Show_Entry.html",context={
        "article": article
    })

def add_arti(request):

        return render(request,"encyclopedia/Add_arti.html",context={
            'name':"name"
    })