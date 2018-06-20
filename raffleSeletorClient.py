import raffleSystem as rs

def isFloat(string): #not my code btw
        try:
            float(string)
            return True
        except ValueError:
            return False

def printReadout(data,disp):
    if disp:
        print("Current data:")
        for key,val in data.items():
            print(">" + key + " : " + val)
        print("")
    print("Please choose an option")
    print("[new] [choose] [quit]")

validNumber = False
while not validNumber:
    premaxc = input("What is the max number of tickets you would like the system to store? (8 reccomended): ")
    if isFloat(premaxc):
        initmaxc = int(premaxc)
        validNumber = True
    else:
        print("Input a number please.")
    disp = False
    dispPeople = input("Display distriuted tickets in readout? y/n : ")
    if dispPeople.lower() == "y" or dispPeople.lower() == "yes":
        disp = True

tickets, maxc = rs.init(initmaxc)
quitting = False
publicTicketData = {}

while not quitting:
    printReadout(publicTicketData,disp)
    choice = input("==> ")
    if choice == "new":
        name = input("Enter Name? ")
        newTik = rs.addTicket(tickets,maxc)
        if newTik == "ERR-MAX_LIMIT_REACHED":
            print("Oops! We're all out of tickets.")
        else:
            publicTicketData[name] = newTik
    elif choice == "quit":
        quitting = True
    elif choice == "choose":
        winner = rs.chooseTicket(tickets,maxc)
        print ("The winner is: {w}".format(w = winner))
        quitting = True

