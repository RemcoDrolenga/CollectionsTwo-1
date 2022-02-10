import random
def SorrySnapIkNiet():
    print ("Sorry dat snap ik niet")


GegooideDobbelStenenList = []


    
# 5 dobbelstenen dobbelen
def DobbelSteenGooienToevoegen(DobbelStenenList ,HoeveelGooien):
    for i in range (HoeveelGooien):
        DobbelSteen = random.randint(1,6)
        DobbelStenenList.append(DobbelSteen)
    print (DobbelStenenList)
    return DobbelStenenList
# print (DobbelSteenGooienToevoegen(5))


    
# vragen welke de speler opnieuw wilt dobbelen
def WilOpnieuwDobbelen(DobbelStenenList):
    WilOpnieuw = input("Wilt u nog een keer gooien? ")
    if WilOpnieuw == "nee" or WilOpnieuw == "N":
        pass
    elif WilOpnieuw == "ja" or WilOpnieuw == "J":
        DoorVragen = 0
        OpnieuwVragen = True
        while DoorVragen <= 4 and OpnieuwVragen == True:
            WelkeOpnieuwGooien = input("Welk nummer wilt u opnieuw gooien? (typ stop als je niet meer opnieuw wilt gooien) ")
            if WelkeOpnieuwGooien == "stop":
                OpnieuwVragen = False
            GetalofNummer = WelkeOpnieuwGooien.isdigit()
            if GetalofNummer == True:
                DobbelStenenList.remove(int(WelkeOpnieuwGooien))
                DobbelSteenDobbelen = random.randint(1, 6)
                DobbelStenenList.append(DobbelSteenDobbelen)
            DoorVragen += 1
        return DobbelStenenList

    else:
        SorrySnapIkNiet()

GegooideDobbelStenen = DobbelSteenGooienToevoegen(GegooideDobbelStenenList, 5)
OngewensteDobbelStenen = WilOpnieuwDobbelen(GegooideDobbelStenenList)
print (OngewensteDobbelStenen)






# Three of a kind: drie dobbelstenen met dezelfde punten
# Four of a  kind: vier dobbelstenen met dezelfde punten
# Full House: 25 punten voor 3 gelijke en een paar (5 gelijke telt niet als full house tenzij het vak Yahtzee reeds is ingevuld.)
# Small straight 0 punten voor vier oplopende dobbelstenen(volgorde maakt niet uit)
# Large straight 40 punten voor 5 oplopende dobbelstenen (Volgorde maakt niet uit)
# Yahtzee (top score) 50 punten 50 punten als alle dobbelsten gelijk zijn
# Chance: totaal aantal punten van alle gegooiden dobbelstenen.