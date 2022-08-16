from django.shortcuts import render
import os
try:
    from dashboard import getfile as getfile_module
    from dashboard import printfile as printfile_module

except Exception as e:
    print("local imports unsuccessful" +str(e))

#Declare new cards in list
card_names=['notewiki','quotes','archieve']
base_dir='notedb'
#Pattern of cards
class Card:

    def __init__(self,name,data,location):
        self.name = name
        self.data= data
        self.location= location
        # self.tag= tag
    
    def givedata(self):
        self.path=os.path.join(base_dir,self.path)
        print("file path passed as request from give data",self.path)
        self.name=getfile_module.getfile(self.path)
        print("\n*****************path",os.path.join(base_dir,self.path))
        self.data=printfile_module.printfile(self.name,False)
        print("\n*****************redirection_path>>>>",self.redirection_path)
        return(self.data,self.redirection_path)

    def printCard(self):
        return('{} {} {}'.format(self.name,self.content,self.tag))

#Class of different cards
class Notewiki(Card):
    path="notes"
    redirection_path="notes"

class Quote(Card):
    path="quotes"
    redirection_path="quotes"

class Archieve(Card):
    path="archieve"
    redirection_path="archieve$"

NotewikiCard= Notewiki("null","null","null")
NotewikiCard.givedata()
# print(help(Notewiki))

QuoteCard= Quote("null","null","null")
QuoteCard.givedata()

ArchieveCard=Archieve("null","null","null")
ArchieveCard.givedata()



card_list=[NotewikiCard,QuoteCard,ArchieveCard]


def create_cards(card_names):
    fullcard=[]
    for card in range(len(card_list)):
        cardobj= Card(card_list[card].name,card_list[card].data, card_list[card].redirection_path)
        print("\n",cardobj.__dict__)
        fullcard.append(cardobj.__dict__)
    return fullcard

# cardDict=create_cards(card_names)
# print(cardDict)

def dashboard(request):
    cards=create_cards(card_names)
    print("\n Passed Cards for render: ",cards)
    context={
        'cards':cards
    }
    print(context)
    return render(request, 'dashboard/dashboard.html',context) 