import random
from turtle import tilt
from django import forms
from django.shortcuts import redirect, render
import markdown2

from encyclopedia.forms import NewPageForm
from . import util


def index(request):
    q = request.GET.get('q')

    entries = util.list_entries()

    t_list=[]
    if q:
        for entry in entries:
            if q == entry:
                article = markdown2.markdown(util.get_entry(entry))
                return render(request,"encyclopedia/Show_Entry.html",context={
                "article": article
                })
            elif q.lower() in entry.lower():
                t_list.append(entry)
                entries = t_list

    return render(request, "encyclopedia/index.html", context={
        "entries": entries,
    })


def Show_Entry(request,title):
    entries = util.list_entries()
    if title in entries:
        article = markdown2.markdown(util.get_entry(title))
        return render(request,"encyclopedia/Show_Entry.html",context={
                "article": article
            })
    else:
        return render(request,"encyclopedia/not_found.html")




def add_arti(request):
    if request.method == "GET":
        add_article_form = forms.NewPageForm()
        return render(request,"encyclopedia/Add_arti.html",context={
            'add':add_article_form,
        })


def random_arti(request):
    ra = random.choice(util.list_entries())
    random_article = markdown2.markdown(util.get_entry(ra))

    return render(request,"encyclopedia/random.html",context={
        "random_article": random_article
    })

