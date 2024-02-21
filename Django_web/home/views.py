from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    links = [(reverse('hello:articles_index'), 'Tech-articles')
             # not automatically yet, we manually add links of different genres
             # (reverse('hello:index2'), 'name')
             ]
    return render(request, 'home/index.html', {
        "links": links
    })
