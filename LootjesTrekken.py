
import random

NamenLijst = []

def NamenVragen(NamenList):
    NamenTellen = 0
    DoorVragen = True
    while DoorVragen == True:
        NaamVragen = input("Welke naam wil je toevoegen? (Typ stop als je geen naam meer wilt toevoegen.) ")
        NaamVragen = NaamVragen.lower()
        if NaamVragen == "stop":
            if len(NamenList) >= 2:
                return NamenList
            else:
                print ("Je moet minimaal 2 namen hebben toegevoegd.")
        NamenTellen += 1
        NamenList.append(NaamVragen)
        NamenListSet = set(NamenList)
        if len(NamenListSet) != NamenTellen: 
            NamenTellen -= 1
            print ("Deze naam heb je al ingevuld.")
            NamenList.remove(NaamVragen)
        

def LootjesTrekken(NamenList):
    ListIndex = 0
    Doorgaan = True
    GetrokkenLootjesDict = {}
    NamenCheckList = []
    NamenCheckSet = set(NamenCheckList)
    HoeveelheidTellen = 0
    while Doorgaan == True:
        NaamKiezen = random.choice(NamenList)
        NamenCheckSet.add(NaamKiezen)
        HoeveelheidTellen += 1
        if len(NamenCheckSet) == HoeveelheidTellen:
            GetrokkenLootjesDict[NamenList[ListIndex]] = NaamKiezen
            ListIndex += 1
        else:
            HoeveelheidTellen -= 1
        if HoeveelheidTellen == len(NamenList):
            Doorgaan = False

    return GetrokkenLootjesDict

def EigenLootjeControle(NamenList, LootjesDict):
    OpnieuwLotenTrekken = LootjesDict
    Opnieuw = True
    OpnieuwLoten = False
    while Opnieuw == True:
        Opnieuw = False
        for key in LootjesDict:
            OpnieuwLoten = False
            if key == LootjesDict[key]:
                OpnieuwLoten = True 
                Opnieuw = True
            else:
                Opnieuw = False
        
        if OpnieuwLoten == True:
            OpnieuwLotenTrekken = LootjesTrekken(LootjesNamen)
        else:
            Opnieuw = False
    
    for key, value in OpnieuwLotenTrekken.items():
        print(key, ' : ', value)


LootjesNamen = NamenVragen(NamenLijst)
LotenTrekken = LootjesTrekken(LootjesNamen)
EigenLootjeControle(LootjesNamen, LotenTrekken)