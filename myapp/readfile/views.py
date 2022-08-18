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
base_dir="notedb"

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
    msg=os.path.join(base_dir,msg)
    # print("\nPassed as request\n",msg)
    args={}
    
    if msg[-1]=="$":
    #   print("*****************One line function called***********")
      new_path=str(msg.rstrip(msg[-1]))
    #   print("\nStripped path\n",new_path)
      filepath=getfile_module.getfile(new_path)
    #   print("\nfilepath passed to getfile:\n",filepath)
      gettext=printfile_module.printfile(filepath,True)
    #   print("\ntext received:\n",gettext)
    else:
    #   print("*****************Multiline function called***********")
      filepath=getfile_module.getfile(msg)
      gettext=printfile_module.printfile(filepath,False)
    # print(gettext)
    args['mytext']=gettext

    lis = list(filepath.split("/"))
    args['author']=lis[len(lis)-1]
    
    return render(request, 'readfile/home.html', args)

def about(request):
    return render(request, 'readfile/about.html') 