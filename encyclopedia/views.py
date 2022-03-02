import random
import markdown2
from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    entries = util.list_entries()
    title = request.POST.get('title')
    markdown = request.POST.get('markdown')

    if not title or not markdown:
        return render(request, "encyclopedia/error.html", {
            "error": "Missing Items",
            "errorMsg": "Please make sure to enter a title and the markdown for your page."
        })

    if title.upper() not in map(str.upper, entries):
        print("successfully added page")
        util.save_entry(title, markdown)
        return redirect(entry, title=title)
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Entry Exists",
            "errorMsg": "This page already exists, please create a new entry and try again."
        })

def edit(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/edit.html", {
            "content": util.get_entry(title),
            "pageTitle": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Not Found",
            "errorMsg": "Hmm, Page Not Found 🤔"
        })

def entry(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(util.get_entry(title)),
            "pageTitle": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Not Found",
            "errorMsg": "Hmm, Page Not Found 🤔"
        })

def new(request):
    return render(request, "encyclopedia/new.html")

def randomPage(request):
    entries = util.list_entries()
    numOfEntries = len(entries)
    randomNum = random.randint(0, numOfEntries - 1)
    title = entries[randomNum]
    return redirect(entry, title=title)

def save(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if not content:
        return render(request, "encyclopedia/error.html", {
            "error": "Missing Content",
            "errorMsg": "Please make sure to enter the markdown for your page."
        })
    util.save_entry(title, content)
    return redirect(entry, title=title)


def search(request):
    entries = util.list_entries()
    query = request.POST.get('q')
    if query.upper() in map(str.upper, entries):
        return redirect(entry, title=query)
    else:
        results = [x for x in map(str.lower, entries) if query.lower() in x]
        return render(request, "encyclopedia/results.html", {
            "results": results
        })