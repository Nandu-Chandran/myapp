import re
import glob
import os
import random
from django.shortcuts import render
from django.http import HttpResponse

try:
    from dashboard import getfile as getfile_module
    from dashboard import printfile as printfile_module


except Exception as e:
    print("local imports unsuccessful" +str(e))


def getfile(path):
  
  final_location=os.path.join(os.getcwd(),path)
  return(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))

def printfile(filename):
  #print(filename)
  with open(filename, "r") as f:
    try:
      file_content = [l for l in (line.strip() for line in f) if l]
      return(random.choice(file_content))
    except:
      return("Empty file")

def index(request):
    # print(para)
    args={}
    filepath=getfile()
    gettext=printfile(filepath)
    args['mytext']=gettext

    lis = list(filepath.split("/"))
    args['author']=lis[len(lis)-1]
    
    return render(request,'readfile/home.html',args)

def viewfile(request,msg):
    
    print(">>>>>>>>>>>>>>>>",msg)
    args={}
    filepath=getfile(msg)
    gettext=printfile(filepath)
    print(gettext)
    args['mytext']=gettext

    lis = list(filepath.split("/"))
    args['author']=lis[len(lis)-1]
    
    return render(request, 'readfile/home.html', args)

def about(request):
    return render(request, 'readfile/about.html') 