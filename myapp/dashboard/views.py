from django.shortcuts import render

# Create your views here.
card_names=['notewiki','reminders','quotes','movielist','musiclist']

class Card:

    def __init__(self,name,context,tag):
        self.name = name
        self.context = context
        self.tag= tag

    def printCard(self):
        return('{} {} {}'.format(self.name,self.context,self.tag))

    # def notewikiCard():


def create_cards(card_names):
    cardList=[]
    for card in range(len(card_names)):
        # print(card)
        cardobj= Card(card_names[card],"null","null")
        cardList.append(cardobj.__dict__)
    return cardList




def dashboard(request):
    cards=create_cards(card_names)
    print(cards)
    context={
        'cards':cards
    }
    print(context)
    return render(request, 'dashboard/dashboard.html',context) 