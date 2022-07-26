try:
    import getfile as getfile_module
    import printfile as printfile_module


except Exception as e:
    print("local imports unsuccessful" +str(e))


card_names=['notewiki','quotes']

class Card:

    def __init__(self,name,content):
        self.name = name
        self.content = content
        # self.tag= tag

    def printCard(self):
        return('{} {} {}'.format(self.name,self.content,self.tag))
    
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

class Quote:
    
    path="myquotes"

    def __init__(self,name,data,tags):
        self.name = name
        self.data = data
        self.tag = tags

    def givedata(self):
        self.name=getfile_module.getfile(self.path)
        self.data=printfile_module.printfile(self.name)
        return(self.data,self.name)


NotewikiCard= Notewiki("null","null","null")
NotewikiCard.givedata()

QuoteCard= Quote("null","null","null")
QuoteCard.givedata()


card_list=[NotewikiCard,QuoteCard]


def create_cards(card_names):
    fullcard=[]
    for card in range(len(card_list)):
        cardobj= Card(card_list[card].name,card_list[card].data)
        fullcard.append(cardobj.__dict__)
    return fullcard

cardDict=create_cards(card_names)
print(cardDict)



