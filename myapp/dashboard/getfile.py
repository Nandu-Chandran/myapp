import os,random,glob
def getfile(dir):
  
  final_location=os.path.join(os.getcwd(),dir)
  # print(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))
  return(random.choice((glob.glob(os.path.join(final_location,"*.txt")))))