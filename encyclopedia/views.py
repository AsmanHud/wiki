from django.shortcuts import render, redirect
import markdown2
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entrytitle):
    entry_md = util.get_entry(entrytitle)
    if entry_md is None:
        return render(request, "encyclopedia/404.html")
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(entry_md),
        "title": entrytitle
    })

def search(request):
    query = request.GET.get('q', '')
    if util.get_entry(query) is not None:
        return entry(request, query)
    else:
        return render(request, "encyclopedia/search.html", {
            "entries": util.query_entries(query),
            "query": query
        })
    
def new(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new.html", {
                "title": title,
                "content": content,
                "error": "Entry already exists."
            })
        else:
            util.save_entry(title, content)
            return redirect('entry', entrytitle=title)
    else:
        return render(request, "encyclopedia/new.html")

def edit(request, entrytitle):
    if request.method == "POST":
        content = request.POST.get('content', '')
        util.save_entry(entrytitle, content)
        return redirect('entry', entrytitle=entrytitle)
    else:
        entry_md = util.get_entry(entrytitle)
        if entry_md is None:
            return render(request, "encyclopedia/404.html")
        return render(request, "encyclopedia/edit.html", {
            "title": entrytitle,
            "content": entry_md
        })

def randompage(request):
    entries = util.list_entries()
    entrytitle = random.choice(entries)
    return redirect('entry', entrytitle=entrytitle)