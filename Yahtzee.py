import random
def VakjeAlIngevuld():
    print ("Dit vakje heb je al inveguld. ")

Hoeveel_Eenen = 0
Hoeveel_Tweeën = 0
Hoeveel_Drieën = 0
Hoeveel_Vieren = 0
Hoeveel_Vijfen = 0
Hoeveel_Zessen = 0


GegooideDobbelStenenList = []


# 5 dobbelstenen dobbelen
def DobbelSteenGooienToevoegen(DobbelStenenList ,HoeveelGooien):
    for i in range (HoeveelGooien):
        DobbelSteen = random.randint(1,1)
        DobbelStenenList.append(DobbelSteen)
    print (DobbelStenenList)
    return DobbelStenenList

    
# vragen welke de speler opnieuw wilt dobbelen
def WilOpnieuwDobbelen(DobbelStenenList):
    BeurtOpnieuw = 0
    while BeurtOpnieuw < 3:
        HoeveelToevoegen = 0
        DoorVragen = 0
        OpnieuwVragen = True
        WilOpnieuw = input("Wil je nog een keer gooien? ")
        if WilOpnieuw == "nee" or WilOpnieuw == "N":
            return DobbelStenenList
        elif WilOpnieuw == "ja" or WilOpnieuw == "J":
            while DoorVragen <= 4 and OpnieuwVragen == True:
                WelkeOpnieuwGooien = input("Welk nummer wil je opnieuw gooien? (typ stop als je niet meer opnieuw wilt gooien) ")
                if WelkeOpnieuwGooien == "stop":
                    OpnieuwVragen = False
                GetalofNummer = WelkeOpnieuwGooien.isdigit()
                if GetalofNummer == True:
                    DobbelStenenList.remove(int(WelkeOpnieuwGooien))
                    HoeveelToevoegen += 1
                DoorVragen += 1
            for i in range (HoeveelToevoegen):
                DobbelSteenDobbelen = random.randint(1, 6)
                DobbelStenenList.append(DobbelSteenDobbelen)
            print (DobbelStenenList)
        BeurtOpnieuw += 1
    return DobbelStenenList

# Three of a kind: drie dobbelstenen met dezelfde punten
# laatste deel werkt nog niet
def ThreeOfAKind(DobbelList):
    DobbelListSet = set(DobbelList)
    DobbelListDict = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}
    if len(DobbelListSet) <= 3:
        for i in (DobbelList):
            DobbelListDict[str(i)] += 1
        # for i in range (6):
        if int('1') in DobbelListDict > 2:
            print ("Je hebt Three of a Kind")
        # print (DobbelListDict)
        

# Four of a  kind: vier dobbelstenen met dezelfde punten
def FourOFAKind(DobbelList):
    pass
# Full House: 25 punten voor 3 gelijke en een paar (5 gelijke telt niet als full house tenzij het vak Yahtzee reeds is ingevuld.)
def FullHouse(DobbelList):
    # set gebruiken
    pass
# Small straight 0 punten voor vier oplopende dobbelstenen(volgorde maakt niet uit)
def SmallStraight(DobbelList):
    DobbelListSet = set(DobbelList)
    DobbelVergelijkList = list(DobbelListSet)
    DobbelList.sort()
    if len(DobbelListSet) >= 4:
        EersteGetalLijst = DobbelList[0]
        DoorTellen = 0
        for i in range (len(DobbelVergelijkList)):
            if EersteGetalLijst == DobbelVergelijkList[i]:
                EersteGetalLijst += 1
                DoorTellen += 1
        if DoorTellen == 4:
                print ("Je hebt een Small Straight. ")
# Large straight 40 punten voor 5 oplopende dobbelstenen (Volgorde maakt niet uit)
def LargeStraight(DobbelList):
    DobbelListSet = set(DobbelList)
    DobbelVergelijkList = list(DobbelListSet)
    DobbelList.sort()
    if len(DobbelListSet) >= 5:
        EersteGetalLijst = DobbelList[0]
        DoorTellen = 0
        for i in range (len(DobbelVergelijkList)):
            if EersteGetalLijst == DobbelVergelijkList[i]:
                EersteGetalLijst += 1
                DoorTellen += 1
        if DoorTellen == 5:
                print ("Je hebt een Large Straight. ")
# Yahtzee (top score) 50 punten 50 punten als alle dobbelsten gelijk zijn
def Yahtzee(DobbelList):
    DobbelListSet = set(DobbelList)
    if len(DobbelListSet) == 1:
        print ("Je hebt Yahtzee.")
    
# Chance: totaal aantal punten van alle gegooiden dobbelstenen.
def Chance(DobbelList):
    pass



# het scoreboord
def ScoreBoord(Eenen, Tweeën, Drieën, Vieren, Vijfen, Zessen):
    OpnieuwBlijvenVragen = True
    while OpnieuwBlijvenVragen == True:
        WelkeInvullen = input("Welk vakje van het scoreboord wil je invullen? ")
        WelkeInvullen = WelkeInvullen.lower()
        if WelkeInvullen == "aces":
            if Eenen > 0:
                VakjeAlIngevuld()
            else:
                Eenen = input("Hoeveel Aces heb je? ")
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "twos":
            if Tweeën > 0:
                VakjeAlIngevuld()
            else:
                Tweeën = input("Hoeveel Twos heb je? ")
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "threes":
            if Drieën > 0:
                VakjeAlIngevuld()
            else:
                Drieën = input("Hoeveel Threes heb je? ")
                OpnieuwBlijvenVragen = False
        elif  WelkeInvullen == "fours":
            if Vieren > 0:
                VakjeAlIngevuld()
            else:
                Vieren = input("Hoeveel Fours heb je? ")
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "fives":
            if Vijfen > 0:
                VakjeAlIngevuld()
            else:
                Vijfen = input("Hoeveel Fives heb je? ")
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "sixes":
            if Zessen > 0:
                VakjeAlIngevuld()
            else:
                OpnieuwBlijvenVragen = False
                Zessen = input("Hoeveel Sixes heb je? ")
        print ("Aces ", Eenen)
        print ("Twos ", Tweeën)
        print ("Threes ", Drieën)
        print ("Fours ", Vieren)
        print ("Fives ", Vijfen)
        print ("Sixes ", Zessen)



GegooideDobbelStenen = DobbelSteenGooienToevoegen(GegooideDobbelStenenList, 5)
print ("")
NieuweDobbelen = WilOpnieuwDobbelen(GegooideDobbelStenenList)
print ("")
# ThreeOfAKind(NieuweDobbelen)
SmallStraight(NieuweDobbelen)
LargeStraight(NieuweDobbelen)
Yahtzee(NieuweDobbelen)
print ("")

ScoreBoord(Hoeveel_Eenen, Hoeveel_Tweeën, Hoeveel_Drieën, Hoeveel_Vieren, Hoeveel_Vijfen, Hoeveel_Zessen)