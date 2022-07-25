import re
import random
from django.shortcuts import render
from django.http import HttpResponse


def getdata():
    with open("notes.txt", "r") as f:
        names_list = [l for l in (line.strip() for line in f) if l]
        return(random.choice(names_list))

# posts=[
#     {
#     'author': 'a',
#     'title': 'first post 1',
#     'content':'content of first'},
#     {
#     'author': 'b',
#     'title': 'first post 2',
#     'content':'content of second'}
#     ]


def index(request):
    
    args={}
    gettext=getdata()
    args['mytext']=gettext
    # context={
    #     'posts':posts
    # }
    return render(request,'readfile/home.html',args)

def about(request):
    return render(request, 'readfile/about.html') 