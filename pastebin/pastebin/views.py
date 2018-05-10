from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from .models import Paste
from .forms import PasteForm


def index(request):
    form = PasteForm()
    ctx = {'form': form}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    paste = Paste.objects.get(pk=id)
    highlighted = highlight(paste.content, PythonLexer(), HtmlFormatter())
    paste.content = highlighted
    ctx = {'paste': paste}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)


def post_paste(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)

        if form.is_valid():
            paste = form.save()
            return HttpResponseRedirect(f'/pastes/{paste.id}/')
