from django.shortcuts import render
import os
from django.urls import reverse


def get_names():
    html_files = [f.split('.')[0] for f in os.listdir('hello/templates/hello')
                  if f.endswith('.html') and (not f.endswith('index.html'))]
    return html_files


def index(request):
    html_files = get_names()
    links = [(reverse(f'hello:{file}'), f'{file}') for file in html_files]
    return render(request, 'hello/articles_index.html', {
        "links": links
    })


def generic_html_view(request, filename):
    template_name = f"hello/{filename}.html"
    return render(request, template_name)
