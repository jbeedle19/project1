from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title),
            "pageTitle": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Not Found",
            "errorMsg": "Hmm, Page Not Found 🤔"
        })

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