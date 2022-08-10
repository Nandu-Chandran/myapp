import os,random
import argparse

def printfile(filename,printfull):
 print("\n>>>>>>filename from printfile function\n",filename)
 with open(filename, "r") as f:
    try:
      file_content = [l for l in (line.strip() for line in f) if l]
      if printfull == True:
        return file_content
      else:
        return(random.choice(file_content))
    except:
      return("Empty file")





# printfile('/home/nc/pjt/pytest/mynotes/digital-minimalism.txt')