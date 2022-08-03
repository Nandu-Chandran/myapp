import os,random
def printfile(filename):
  # print(filename)
  with open(filename, "r") as f:
    try:
      file_content = [l for l in (line.strip() for line in f) if l]
      #print(random.choice(file_content))
      return(random.choice(file_content))
    except:
      return("Empty file")

# printfile('/home/nc/pjt/pytest/mynotes/digital-minimalism.txt')