from django.shortcuts import render

try:
    from dashboard import getfile as getfile_module
    from dashboard import printfile as printfile_module


except Exception as e:
    print("local imports unsuccessful" +str(e))

#Declare new cards in list
card_names=['notewiki','quotes']

#Pattern of cards
class Card:

    def __init__(self,name,content,redirection_path):
        self.name = name
        self.content = content
        self.redirection_path= redirection_path
        # self.tag= tag

    def printCard(self):
        return('{} {} {}'.format(self.name,self.content,self.tag))
    
    # def notewikiCard(self):
#Class of different cards
class Notewiki:
    
    path="notes"
    redirection_path="notes"

    def __init__(self,name,data,tags):
        # self.path = Notewiki.path
        self.name = name
        self.data = data
        self.tag = tags

    def givedata(self):
        # self.path="mynotes"
        self.name=getfile_module.getfile(self.path)
        self.data=printfile_module.printfile(self.name)
        return(self.data,self.redirection_path)

class Quote:
    
    path="quotes"
    redirection_path="quotes"

    def __init__(self,name,data,tags):
        self.name = name
        self.data = data
        self.tag = tags

    def givedata(self):
        self.name=getfile_module.getfile(self.path)
        self.data=printfile_module.printfile(self.name)
        return(self.data,self.name,self.redirection_path)


NotewikiCard= Notewiki("null","null","null")
NotewikiCard.givedata()

QuoteCard= Quote("null","null","null")
QuoteCard.givedata()


card_list=[NotewikiCard,QuoteCard]


def create_cards(card_names):
    fullcard=[]
    for card in range(len(card_list)):
        cardobj= Card(card_list[card].name,card_list[card].data, card_list[card].redirection_path)
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
    # print(context)
    return render(request, 'dashboard/dashboard.html',context) 