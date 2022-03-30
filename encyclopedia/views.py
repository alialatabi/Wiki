import random
from turtle import tilt
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import markdown2
from django.contrib import messages
from encyclopedia.forms import EditArticleForm, NewArticleForm
from . import util
from encyclopedia.forms import NewArticleForm




def index(request):
    entries = util.list_entries()
    q = request.GET.get('q')
    search = False
    t_list=[]
    if q:
        search = True
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
        "SearchP": search
    })


def Show_Entry(request,title):
    entries = util.list_entries()
    if title in entries:
        article = markdown2.markdown(util.get_entry(title))
        return render(request,"encyclopedia/Show_Entry.html",context={
                "title":title,
                "article": article
            })
    else:
        return render(request,"encyclopedia/not_found.html")


def add_arti(request):
    entries = util.list_entries()
    if request.method == "GET":
        return render(request,"encyclopedia/Add_arti.html",context={
            'add':NewArticleForm(),
        })

    if request.method == "POST":
        arti = NewArticleForm(request.POST)
        if arti.is_valid():
            title = arti.cleaned_data["title"]
            content = arti.cleaned_data["content"]
            if title in entries:
                return render(request,"encyclopedia/Add_arti.html",context={
                    "e_check": True
                    })
            else:
                util.save_entry(title,content)
                return redirect(index)

def edit(request,title:str):
    entries = util.list_entries()
    if request.method == "GET":
        article = util.get_entry(title)
        return render(request,"encyclopedia/edit.html",context={
            'edit':EditArticleForm(initial={'content': article}),
            'title': title,
        })

    if request.method == "POST":
        arti = EditArticleForm(request.POST)
        if arti.is_valid():
            content = arti.cleaned_data["content"]
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse("index"))


def random_arti(request):
    entries = util.list_entries()
    ra = random.choice(entries)
    random_article = markdown2.markdown(util.get_entry(ra))

    return redirect(Show_Entry,title=ra)

