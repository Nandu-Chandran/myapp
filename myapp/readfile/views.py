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


def index(request):
    # print(para)
    args={}
    filepath=getfile_module()
    gettext=printfile_module(filepath)
    args['mytext']=gettext

    lis = list(filepath.split("/"))
    args['author']=lis[len(lis)-1]
    
    return render(request,'readfile/home.html',args)

def viewfile(request,msg):
    
    print(">>>>>>>>>>>>>>>>",msg)
    args={}
    filepath=getfile_module.getfile(msg)
    gettext=printfile_module.printfile(filepath)
    print(gettext)
    args['mytext']=gettext

    lis = list(filepath.split("/"))
    args['author']=lis[len(lis)-1]
    
    return render(request, 'readfile/home.html', args)

def about(request):
    return render(request, 'readfile/about.html') 