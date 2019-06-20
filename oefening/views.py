from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import os
import re
import requests
import json

from oefening.models import PersonForm
from oefening.models import Person


def index(request):
    return HttpResponse("weed")


def test(request, number):
    return HttpResponse("You're looking at question %s." % number)


def apike(request):

    namen = Person.objects.all().last()
    print(namen)
    url = 'http://api.icndb.com/jokes/random'
    urlNames = '?firstName='+namen.voornaam + '&lastName=' + namen.achternaam

    r = requests.get(url + urlNames)
    data = r.json()

    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            saved = form.save(commit=True)
            form.cleaned_data
            obj = Person.objects.all().last()
            qcontext = {
                'naam': obj,
                # 'savedForm': PersonForm(instance=saved)
            }
            return render(request, 'oefening/jokeApi.html', qcontext)

    context = {
        'id': data['value']['id'],
        'joke': data['value']['joke'],
        'form': form
    }

    return render(request, 'oefening/jokeApi.html', context)


def song(request):
    file = 'oefening/txtfile/song.txt'

    with open(file) as f:
        context = {'songs': f}
        return render(request, 'oefening/songs.html', context)


def movies(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'txtfile/movies.txt')
    data_file = open(file_path, 'r')
    # data = data_file.read()
    context = {'movies': data_file}
    return render(request, 'oefening/movies.html', context)

    """
    f = open(file, 'r')
    file_content = f.readLines()
    f.close()
    """

    """
 with open(file) as f:
        a = f.readlines()
        f.seek(0)
        b = f.readline()
        context = {'songs': a}

    """

    """
     with open(file) as f:
        fl = f.readlines()
        for x in fl:
            context = {'songs': x}
            return render(request, 'oefening/songs.html', context)
    """
