import os,random,glob
def getfile(dir):
  try:
    final_location=os.path.join(os.getcwd(),dir)
    print("*****final_location of text file*********",final_location)
    # print(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))
    return(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))
  except:
    print("Cannot find file")