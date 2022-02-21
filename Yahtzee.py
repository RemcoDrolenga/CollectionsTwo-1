import random
def VakjeAlIngevuld():
    print ("Dit vakje heb je al inveguld. ")


RondeTellen = 0
NogEenKeer = True
HoevaakIngevuld = 0


# GegooideDobbelStenenList = []
ScoreBoordDictPart1 = {"Aces" : 0,"Twos" : 0,"Threes" : 0, "Fours" : 0, "Fives" : 0, "Sixes" : 0,"Total" : 0, "Bonus" : 0}
ScroeBoordDictPart2 = {}

# 5 dobbelstenen dobbelen
def DobbelSteenGooienToevoegen(DobbelStenenList ,HoeveelGooien):
    for i in range (HoeveelGooien):
        DobbelSteen = random.randint(1,6)
        DobbelStenenList.append(DobbelSteen)
    print (DobbelStenenList)
    return DobbelStenenList

    
# vragen welke de speler opnieuw wilt dobbelen
def WilOpnieuwDobbelen(DobbelStenenList):
    BeurtOpnieuw = 0
    while BeurtOpnieuw < 2:
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
def ThreeOfAKind(DobbelList):
    DobbelListSet = set(DobbelList)
    DobbelListDict = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}
    if len(DobbelListSet) <= 3:
        for i in (DobbelList):
            DobbelListDict[str(i)] += 1
        for key in DobbelListDict:
            if DobbelListDict[key] == 3:
                print ("Je hebt Three of a Kind. ")
        

# Four of a  kind: vier dobbelstenen met dezelfde punten
def FourOFAKind(DobbelList):
    DobbelListSet = set(DobbelList)
    DobbelListDict = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}
    if len(DobbelListSet) <= 2:
        for i in (DobbelList):
            DobbelListDict[str(i)] += 1
        for key in DobbelListDict:
            if DobbelListDict[key] >= 4:
                print ("Je hebt Four of a Kind. ")
# Full House: 25 punten voor 3 gelijke en een paar (5 gelijke telt niet als full house tenzij het vak Yahtzee reeds is ingevuld.)
def FullHouse(DobbelList):
    DobbelListSet = set(DobbelList)
    DobbelListDict = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}
    if len(DobbelListSet) <= 2:
        for i in (DobbelList):
            DobbelListDict[str(i)] += 1
        for key in DobbelListDict:
            if DobbelListDict[key] == 3:
                for x in DobbelListDict:
                    if DobbelListDict[x] == 2:
                        print ("Je hebt een Full House. ")
# Small straight 30 punten voor vier oplopende dobbelstenen(volgorde maakt niet uit)
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
# Yahtzee (top score) 50 punten als alle dobbelstenen gelijk zijn
def Yahtzee(DobbelList):
    DobbelListSet = set(DobbelList)
    if len(DobbelListSet) == 1:
        print ("Je hebt Yahtzee. ")
    
# Chance: totaal aantal punten van alle gegooiden dobbelstenen.
def Chance(DobbelList):
    TotaalPunten = sum(DobbelList)
    print ("Chance is:", TotaalPunten)



# het scoreboord
def ScoreBoord(ScoreDictPart1,HoevaakIngevuld):
    TotaalPunten = 0
    OpnieuwBlijvenVragen = True
    while OpnieuwBlijvenVragen == True:
        WelkeInvullen = input("Welk vakje van het scoreboord wil je invullen? ")
        WelkeInvullen = WelkeInvullen.lower()
        if WelkeInvullen == "aces":
            if ScoreDictPart1["Aces"] > 0:
                VakjeAlIngevuld()
            else:
                Eenen = int(input("Hoeveel Aces heb je? "))
                HoevaakIngevuld += 1
                ScoreDictPart1["Aces"] = Eenen
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "twos":
            if ScoreDictPart1["Twos"] > 0:
                VakjeAlIngevuld()
            else:
                Tweeën = int(input("Hoeveel Twos heb je? "))
                HoevaakIngevuld += 1
                ScoreDictPart1["Twos"] = Tweeën
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "threes":
            if ScoreDictPart1["Threes"] > 0:
                VakjeAlIngevuld()
            else:
                Drieën = int(input("Hoeveel Threes heb je? "))
                HoevaakIngevuld += 1
                ScoreDictPart1["Threes"] = Drieën
                OpnieuwBlijvenVragen = False
        elif  WelkeInvullen == "fours":
            if ScoreDictPart1["Fours"] > 0:
                VakjeAlIngevuld()
            else:
                Vieren = int(input("Hoeveel Fours heb je? "))
                HoevaakIngevuld += 1
                ScoreDictPart1["Fours"] = Vieren
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "fives":
            if ScoreDictPart1["Fives"] > 0:
                VakjeAlIngevuld()
            else:
                Vijfen = int(input("Hoeveel Fives heb je? "))
                HoevaakIngevuld += 1
                ScoreDictPart1["Fives"] = Vijfen
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "sixes":
            if ScoreDictPart1["Sixes"] > 0:
                VakjeAlIngevuld()
            else:
                Zessen = int(input("Hoeveel Sixes heb je? "))
                OpnieuwBlijvenVragen = False
                HoevaakIngevuld += 1
                ScoreDictPart1["Sixes"] = Zessen
        if HoevaakIngevuld == 6:
            Values = ScoreDictPart1.values()
            TotaalPunten = sum(Values)
            ScoreDictPart1["Total"] = TotaalPunten
        if TotaalPunten >= 63:
            print ("Je hebt 35 bonus punten")
            ScoreDictPart1["Bonus"] = 35
        print (ScoreDictPart1)
        print ("")


while RondeTellen < 13 and NogEenKeer == True:
    NogEenKeer = True
    GegooideDobbelStenenList = []
    GegooideDobbelStenen = DobbelSteenGooienToevoegen(GegooideDobbelStenenList, 5)
    print ("")
    NieuweDobbelen = WilOpnieuwDobbelen(GegooideDobbelStenenList)
    print ("")
    ThreeOfAKind(NieuweDobbelen)
    FourOFAKind(NieuweDobbelen)
    FullHouse(NieuweDobbelen)
    SmallStraight(NieuweDobbelen)
    LargeStraight(NieuweDobbelen)
    Yahtzee(NieuweDobbelen)
    Chance(NieuweDobbelen)
    print ("")

    ScoreBoord(ScoreBoordDictPart1,HoevaakIngevuld)
    NogEenRonde = input("Wil je nog een ronde spelen? ")
    if NogEenRonde == "ja":
        NogEenKeer = True
    else:
        NogEenKeer = False
    RondeTellen += 1