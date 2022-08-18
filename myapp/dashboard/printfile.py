import os,random
import argparse

def printfile(filename,printfull):
#  print("\n>>>>>>filename from printfile function\n",filename)
 with open(filename, "r") as file:
    try:
      if printfull == True:
         file_content= fulldisplay(file)
         return file_content
      else:
         file_content = [l for l in (line.strip() for line in file) if l]
         return(random.choice(file_content))
    except:
      return("Empty file")

def fulldisplay(file_obj):
  content= file_obj.read()
  return content





# printfile('/home/nc/pjt/pytest/mynotes/digital-minimalism.txt')