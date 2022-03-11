# Vraag namen op van deelnemers --- gedaan
# Controleer telkens of een ingevoerde naam wel uniek is --- gedaan
# Als er meer dan 2 namen zijn opgegeven kunnen er lootjes worden getrokken --- gedaan
# Maak lootjes voor alle namen -- gedaan
# Trek voor alle namen willekeurig (random) een lootje -- gedaan
# Iedereen heeft dus één uniek lootje
# Niemand mag het lootje van zichzelf hebben getrokken
# Print een lijst met namen en bijbehorende lootjes
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
    for key, value in GetrokkenLootjesDict.items():
        print(key, ' : ', value)

    print ("Opnieuw")
    return GetrokkenLootjesDict

def EigenLootjeControle(NamenList, LootjesDict):
    OpnieuwLotenTrekken = LootjesDict
    Opnieuw = True
    OpnieuwLoten = False
    while Opnieuw == True:
        Opnieuw = False
        for key in LootjesDict:
            if key == LootjesDict[key]:
                print ("Niet Goed")
                OpnieuwLoten = True 
                Opnieuw = True
            # else:
            #     Opnieuw = False
        
        print (OpnieuwLoten)
        if OpnieuwLoten == True:
            OpnieuwLotenTrekken = LootjesTrekken(LootjesNamen)
            print ("Test")
        else:
            Opnieuw = False
    
    for key, value in OpnieuwLotenTrekken.items():
        print(key, ' : ', value)


LootjesNamen = NamenVragen(NamenLijst)
LotenTrekken = LootjesTrekken(LootjesNamen)
EigenLootjeControle(LootjesNamen, LotenTrekken)