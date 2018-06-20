import random

def init(maxDigits):
    tickets = []
    maxdigits = maxDigits
    return tickets, maxdigits

def addTicket(tickets, maxdigits):
    newTicket = str(len(tickets)+1)
    if len(tickets) > (1*(10 **maxdigits)):
        print("Can't add any more tickets. Max limit of {l} reached.".format(l =(1*(10 **maxdigits))))
        return "ERR-MAX_LIMIT_REACHED"
    else:
        newTicket = ("0" * (maxdigits-len(newTicket))) + newTicket
        tickets.append(newTicket)
        return newTicket
    
def chooseTicket(tickets,maxd):
    for i in range((1*(10 **maxd))-len(tickets)):
        addTicket(tickets,maxd)
    random.seed(a=None)
    winnerIndex = random.randrange(0,len(tickets))
    winner = tickets[winnerIndex]
    return winner

#TODO: add save
