from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import os
import re
import requests
import json
import random




def index(request):
    file = 'oefening/txtfile/numbers.txt'
    with open(file) as f:
        context = {'nr': f}
        return render(request, 'oefening/nrkes.html', context)

def nummerkes(request,line1,line2):
    context = {
        'line1': line1,
        'line2': line2
    }
    return render(request, 'oefening/nrkes.html', context)


def lijsteke(request,a,b):
    lijst = [112,245,14,7,28,200,5386,12,17,11,13478,23,26,18,9999]
    for i in range(min(lijst),max(lijst)):
        try:
            context = {
                'a': lijst[a],
                'b': b
            }
            return render(request, 'oefening/nrkes.html', context)

        except Exception as e:
            print(type(e))









