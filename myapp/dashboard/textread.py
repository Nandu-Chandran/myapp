try:
    import getfile as getfile_module
    import printfile as printfile_module


except Exception as e:
    print("local imports unsuccessful" +str(e))


card_names=['notewiki','reminders','quotes','movielist','musiclist']

class Card:

    def __init__(self,name,context,tag):
        self.name = name
        self.context = context
        self.tag= tag

    def printCard(self):
        return('{} {} {}'.format(self.name,self.context,self.tag))
    
    # def notewikiCard(self):

class Notewiki:
    
    path="mynotes"

    def __init__(self,name,data,tags):
        # self.path = Notewiki.path
        self.name = name
        self.data = data
        self.tag = tags

    def givedata(self):
        # self.path="mynotes"
        self.name=getfile_module.getfile(self.path)
        self.data=printfile_module.printfile(self.name)
        return(self.data)


class Quotes:
    

    def __init__(self,name,path,data,tags):
        self.path = path
        self.name = name
        self.data = data
        self.tag = tags

    def givedata(self):
        self.path="mynotes"
        self.name=getfile_module.getfile(self.path)
        self.data=printfile_module.printfile(self.name)
        return(self.data)


def create_cards(card_names):
    fullcard=[]
    for card in range(len(card_names)):
        # print(card)
        cardobj= Card(card_names[card],"null","null")

        fullcard.append(cardobj.__dict__)
    return fullcard

cardDict=create_cards(card_names)
print(cardDict)

mynotes="mynotes"
NotewikiCard= Notewiki("null","null","null")
NotewikiCard.givedata()
print(">",NotewikiCard.data)