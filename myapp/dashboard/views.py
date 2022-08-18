from secrets import randbelow
import random
from django.shortcuts import render,redirect
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
        # print("file path passed as request from give data",self.path)
        self.name=getfile_module.getfile(self.path)
        # print("\n*****************path",os.path.join(base_dir,self.path))
        self.data=printfile_module.printfile(self.name,False)
        # print("\n*****************redirection_path>>>>",self.redirection_path)
        return(self.data,self.redirection_path)

    def printCard(self):
        return('{} {} {}'.format(self.name,self.content,self.tag))

#Class of different cards
class Commonplace(Card):
    path="commonplace"
    redirection_path="commonplace"

class Notewiki(Card):
    path="notes"
    redirection_path="notes"

class Quote(Card):
    path="quotes"
    redirection_path="quotes"

class Archieve(Card):
    path="archieve"
    redirection_path="archieve$"

CommonplaceCard= Commonplace("null","null","null")
CommonplaceCard.givedata()

NotewikiCard= Notewiki("null","null","null")
NotewikiCard.givedata()
# # print(help(Notewiki))

QuoteCard= Quote("null","null","null")
QuoteCard.givedata()

ArchieveCard=Archieve("null","null","null")
ArchieveCard.givedata()


# card_class=['Notewiki','Quote','Archieve']
# Obj="Card"
# def create_obj(card_class):
#     # for card in card_class:
#         tmp=card_class[0]("null","null","null") 
#         print("inloop")
#         tmp.givedata()

# create_obj(card_class)
card_display_order=[QuoteCard,CommonplaceCard,NotewikiCard,ArchieveCard]


def create_cards(card_names):
    fullcard=[]
    for card in range(len(card_display_order)):
        cardobj= Card(card_display_order[card].name,card_display_order[card].data, card_display_order[card].redirection_path)
        #print("\n",cardobj.__dict__)
        fullcard.append(cardobj.__dict__)
    return fullcard

# cardDict=create_cards(card_names)
# print(cardDict)

def dashboard(request):
    cards={}
    context={'cards':" "}
    # if(request.method=='GET'):
    
    # print("empty context",context)
    list1 = [1, 2, 3, 4, 5, 6]
    # print("random value:---->",random.choice(list1))
    cards=create_cards(card_names)
    #print("\n Passed Cards for render: ",cards)
    context={
        'cards':cards
    }
    # print(context)
    return render(request, 'dashboard/dashboard.html',context)


# def refresh(a):
#     print("****************refreshed******")
#     dashboard(a)
    