from turtle import tilt
from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def Show_Entry(request):
    return render(request,"encyclopedia/Show_Entry.html",{
        "article": markdown2.markdown(util.get_entry('CSS'))
    })
