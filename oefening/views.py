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
     return HttpResponse("line1 = %s" % line1)


# def index(request):
#     return HttpResponse("hallo")


# def test(request, number):
#     return HttpResponse("You're looking at question %s." % number)




