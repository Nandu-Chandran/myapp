import os,random,glob
def getfile(dir):
  try:
    # print("directory name received by getfile fun",dir)
    final_location=os.path.join(os.getcwd(),dir)
    # print("\nlocation of text file\n",final_location)
    # print(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))
    return(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))
  except:
    print("Cannot find file")