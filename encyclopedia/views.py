from django.shortcuts import render

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