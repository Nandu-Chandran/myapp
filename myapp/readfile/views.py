import re
import glob
import os
import random
from django.shortcuts import render
from django.http import HttpResponse


def getfile():
  os.chdir("./mynotes")
  return(random.choice((glob.glob("*.txt"))))


def printfile(filename):
  print(filename)
  with open(filename, "r") as f:
    try:
      file_content = [l for l in (line.strip() for line in f) if l]
      print(random.choice(file_content))
    except:
      print("Empty file")
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