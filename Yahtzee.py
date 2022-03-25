import random
def VakjeAlIngevuld():
    print ("Dit vakje heb je al inveguld. ")


RondeTellen = 0
NogEenKeer = True
HoevaakIngevuld = 0
HoevaakIngevuldPart2 = 0



ScoreBoordDictPart1 = {"Aces" : 0,"Twos" : 0,"Threes" : 0, "Fours" : 0, "Fives" : 0, "Sixes" : 0,"Total" : 0, "Bonus" : 0}
ScoreBoordDictPart2 = {"Three Of A Kind" : 0, "Four Of A Kind" : 0, "Full House" : 0, "Small Straight" : 0,"Large Straight" : 0, "Yahtzee" : 0, "Chance" : 0, "TotalPart1" : 0, "TotalPart2" : 0, "Total" : 0}
CombinatieBooleans = {"Three Of A Kind" : False, "Four Of A Kind" : False, "Full House" : False, "Small Straight" : False, "Large Straight" : False, "Yahtzee" : False}
CombinatieBooleansIngevuld = {"Three Of A Kind" : True, "Four Of A Kind" : True, "Full House" : False, "Small Straight" : True, "Large Straight" : True, "Yahtzee" : True, "Chance" : True}

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
def ThreeOfAKind(DobbelList, BoolDict):
    DobbelListSet = set(DobbelList)
    DobbelListDict = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}
    if len(DobbelListSet) <= 3:
        for i in (DobbelList):
            DobbelListDict[str(i)] += 1
        for key in DobbelListDict:
            if DobbelListDict[key] == 3:
                print ("Je hebt Three of a Kind. ")
                BoolDict["Three Of A Kind"] = True
    return BoolDict

# Four of a  kind: vier dobbelstenen met dezelfde punten
def FourOFAKind(DobbelList, BoolDict):
    DobbelListSet = set(DobbelList)
    DobbelListDict = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}
    if len(DobbelListSet) <= 2:
        for i in (DobbelList):
            DobbelListDict[str(i)] += 1
        for key in DobbelListDict:
            if DobbelListDict[key] >= 4:
                print ("Je hebt Four of a Kind. ")
                BoolDict["Four Of A Kind"] = True
    return BoolDict

# Full House: 25 punten voor 3 gelijke en een paar (5 gelijke telt niet als full house tenzij het vak Yahtzee reeds is ingevuld.)
def FullHouse(DobbelList, BoolDict):
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
                        BoolDict["Full House"] = True
    return BoolDict

# Small straight 30 punten voor vier oplopende dobbelstenen(volgorde maakt niet uit)
def SmallStraight(DobbelList, BoolDict):
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
        if DoorTellen >= 4:
            BoolDict["Small Straight"] = True

    return BoolDict

# Large straight 40 punten voor 5 oplopende dobbelstenen (Volgorde maakt niet uit)
def LargeStraight(DobbelList, BoolDict):
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
                BoolDict["Large Straight"] = True
    return BoolDict

# Yahtzee (top score) 50 punten als alle dobbelstenen gelijk zijn
def Yahtzee(DobbelList, BoolDict):
    DobbelListSet = set(DobbelList)
    if len(DobbelListSet) == 1:
        print ("Je hebt Yahtzee. ")
        BoolDict["Yahtzee"] = True
    return BoolDict
    
# Chance: totaal aantal punten van alle gegooiden dobbelstenen.
def Chance(DobbelList):
    TotaalPunten = sum(DobbelList)
    print ("Chance is:", TotaalPunten)



# het scoreboord
def ScoreBoord(ScoreDictPart1,ScoreDictPart2,HoevaakIngevuldPart1, DobbelList, CombinatieDict, HoevaakIngevuldPart2, BoolList):
    TotaalOgen = sum(DobbelList)
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
                HoevaakIngevuldPart1 += 1
                ScoreDictPart1["Aces"] = Eenen
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "twos":
            if ScoreDictPart1["Twos"] > 0:
                VakjeAlIngevuld()
            else:
                Tweeën = int(input("Hoeveel Twos heb je? "))
                HoevaakIngevuldPart1 += 1
                ScoreDictPart1["Twos"] = Tweeën
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "threes":
            if ScoreDictPart1["Threes"] > 0:
                VakjeAlIngevuld()
            else:
                Drieën = int(input("Hoeveel Threes heb je? "))
                HoevaakIngevuldPart1 += 1
                ScoreDictPart1["Threes"] = Drieën
                OpnieuwBlijvenVragen = False
        elif  WelkeInvullen == "fours":
            if ScoreDictPart1["Fours"] > 0:
                VakjeAlIngevuld()
            else:
                Vieren = int(input("Hoeveel Fours heb je? "))
                HoevaakIngevuldPart1 += 1
                ScoreDictPart1["Fours"] = Vieren
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "fives":
            if ScoreDictPart1["Fives"] > 0:
                VakjeAlIngevuld()
            else:
                Vijfen = int(input("Hoeveel Fives heb je? "))
                HoevaakIngevuldPart1 += 1
                ScoreDictPart1["Fives"] = Vijfen
                OpnieuwBlijvenVragen = False
        elif WelkeInvullen == "sixes":
            if ScoreDictPart1["Sixes"] > 0:
                VakjeAlIngevuld()
            else:
                Zessen = int(input("Hoeveel Sixes heb je? "))
                OpnieuwBlijvenVragen = False
                HoevaakIngevuldPart1 += 1
                ScoreDictPart1["Sixes"] = Zessen
        if HoevaakIngevuldPart1 == 6:
            Values = ScoreDictPart1.values()
            TotaalPunten = sum(Values)
            ScoreDictPart1["Total"] = TotaalPunten
            TotaalPuntenPart1 = TotaalPunten
        if TotaalPunten >= 63:
            print ("Je hebt 35 bonus punten")
            ScoreDictPart1["Bonus"] = 35
            TotaalPuntenPart1 += 35

        if WelkeInvullen == "three of a kind":
            if BoolList["Three Of A Kind"] == True:
                BoolList["Three Of A Kind"] = False
                HoevaakIngevuldPart2 += 1
                OpnieuwBlijvenVragen = False
                if CombinatieDict["Three Of A Kind"] == True:
                    ScoreDictPart2["Three Of A Kind"] = TotaalOgen
                else:
                    ScoreDictPart2["Three Of A Kind"] = 0
            else:
                VakjeAlIngevuld()
        elif WelkeInvullen == "four of a kind":
                if BoolList["Four Of A Kind"] == True:
                    BoolList["Four Of A Kind"] = False
                    HoevaakIngevuldPart2 += 1
                    OpnieuwBlijvenVragen = False
                    if CombinatieDict["Four Of A Kind"] == True:
                        ScoreDictPart2["Four Of A Kind"] = TotaalOgen
                    else:
                        ScoreDictPart2["Four Of A Kind"] = 0
                else:
                    VakjeAlIngevuld()
        elif WelkeInvullen == "full house":
            if BoolList["Full House"] == True:
                BoolList["Full House"] = False
                HoevaakIngevuldPart2 += 1
                OpnieuwBlijvenVragen = False
                if CombinatieDict["Full House"] == True:
                    ScoreDictPart2["Full House"] = 25
                else:
                    ScoreDictPart2["Full House"] = 0
            else:
                VakjeAlIngevuld()
        elif WelkeInvullen == "small straight":
            if BoolList["Small Straight"] == True:
                BoolList["Small Straight"] = False
                HoevaakIngevuldPart2 += 1
                OpnieuwBlijvenVragen = False
                if CombinatieDict["Small Straight"] == True:
                    ScoreDictPart2["Small Straight"] = 30
                else:
                    ScoreDictPart2["Small Straight"] = 0
            else:
                VakjeAlIngevuld()
        elif WelkeInvullen == "large straight":
            if BoolList["Large Straight"] == True:
                BoolList["Large Straight"] = False
                HoevaakIngevuldPart2 += 1
                OpnieuwBlijvenVragen = False
                if CombinatieDict["Large Straight"] == True:
                    ScoreDictPart2["Large Straight"] = 40
                else:
                    ScoreDictPart2["Large Straight"] = 0
            else:
                VakjeAlIngevuld()
        elif WelkeInvullen == "yahtzee":
            if BoolList["Yahtzee"] == True:
                BoolList["Yahtzee"] = False
                HoevaakIngevuldPart2 += 1
                OpnieuwBlijvenVragen = False
                if CombinatieDict["Yahtzee"] == True:
                    ScoreDictPart2["Yahtzee"] = 50
                else:
                    ScoreDictPart2["Yahtzee"] = 0
            else:
                VakjeAlIngevuld()
        elif WelkeInvullen == "chance":
            if BoolList["Chance"] == True:
                BoolList["Chance"] = False
                HoevaakIngevuldPart2 += 1
                OpnieuwBlijvenVragen = False
                ScoreBoordDictPart2["Chance"] = TotaalOgen
            else:
                VakjeAlIngevuld()
        if HoevaakIngevuldPart2 == 7:
            ValuesPart2 = ScoreBoordDictPart2.values()
            TotaalPuntenPart2 = sum(ValuesPart2)
            ScoreBoordDictPart2["TotalPart2"] = TotaalPuntenPart2
            ScoreBoordDictPart2["TotalPart1"] = TotaalPuntenPart1
            TotaalPuntenPart1_2 = TotaalPuntenPart2 + TotaalPuntenPart1
            ScoreBoordDictPart2["Total"] = TotaalPuntenPart1_2
        for key, value in ScoreDictPart1.items():
            print(key, ' : ', value)
        for key, value in ScoreBoordDictPart2.items():
            print(key, ' : ', value)
        print ("")


while RondeTellen < 13 and NogEenKeer == True:
    RondeTellen += 1
    print ("Ronde", RondeTellen)
    NogEenKeer = True
    GegooideDobbelStenenList = []
    GegooideDobbelStenen = DobbelSteenGooienToevoegen(GegooideDobbelStenenList, 5)
    print ("")
    NieuweDobbelen = WilOpnieuwDobbelen(GegooideDobbelStenenList)
    print ("")
    Three_Kind = ThreeOfAKind(NieuweDobbelen, CombinatieBooleans)
    Four_Kind = FourOFAKind(NieuweDobbelen, CombinatieBooleans)
    Full_House = FullHouse(NieuweDobbelen, CombinatieBooleans)
    Small_Straight = SmallStraight(NieuweDobbelen, CombinatieBooleans)
    Large_Straight = LargeStraight(NieuweDobbelen, CombinatieBooleans)
    YahtzeeFunctie = Yahtzee(NieuweDobbelen, CombinatieBooleans)
    Chance(NieuweDobbelen)
    print ("")

    ScoreBoord(ScoreBoordDictPart1,ScoreBoordDictPart2,HoevaakIngevuld, NieuweDobbelen, YahtzeeFunctie,HoevaakIngevuldPart2, CombinatieBooleansIngevuld)
    NogEenRonde = input("Wil je nog een ronde spelen? ")
    if NogEenRonde == "ja":
        NogEenKeer = True
    else:
        NogEenKeer = False
