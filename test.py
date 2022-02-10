import random
def SorrySnapIkNiet():
    print ("Sorry dat snap ik niet")

GegooideDobbelStenenList = []

DobbelSteen1Opnieuw = False
DobbelSteen2Opnieuw = False
DobbelSteen3Opnieuw = False
DobbelSteen4Opnieuw = False
DobbelSteen5Opnieuw = False

# Toevoegen en verwijderen
def DobbelSteenOpnieuwGooien(VerwijderDobbelSteen):
    GegooideDobbelStenenList.remove(VerwijderDobbelSteen)
    DobbelSteen = random.randint(1,6)
    GegooideDobbelStenenList.append(DobbelSteen)
    return GegooideDobbelStenenList
    
# 5 dobbelstenen dobbelen
def DobbelSteenGooienToevoegen(x):
    for i in range (x):
        DobbelSteen = random.randint(1,6)
        GegooideDobbelStenenList.append(DobbelSteen)
    return GegooideDobbelStenenList
print (DobbelSteenGooienToevoegen(5))

# gewenste dobbelstenen vervangen
def DobbelStenenVervangen(DobbelSteenOpnieuw):
    if DobbelSteenOpnieuw == True:
        print (DobbelSteenOpnieuwGooien(1))
    if DobbelSteen2Opnieuw == True:
        print (DobbelSteenOpnieuwGooien(2))
    if DobbelSteen3Opnieuw == True:
        print (DobbelSteenOpnieuwGooien(3))
    if DobbelSteen4Opnieuw == True:
        print (DobbelSteenOpnieuwGooien(4))
    if DobbelSteen5Opnieuw == True:
        print (DobbelSteenOpnieuwGooien(5))
    print (DobbelSteenGooien())

# vragen welke de speler opnieuw wilt dobbelen
def WilOpnieuwDobbelen():
    WilOpnieuw = input("Wilt u nog een keer gooien? ")
    if WilOpnieuw == "nee" or WilOpnieuw == "N":
        pass
    elif WilOpnieuw == "ja" or WilOpnieuw == "J":
        while VraagHerhalen <= 6 and VraagStoppen == True:
            WelkeOpnieuwGooien = input("Welk nummer wilt u opnieuw gooien? (typ stop als je er geen meer opnieuw wilt gooien) ")
            if WelkeOpnieuwGooien == "nee" or WelkeOpnieuwGooien == "N":
                pass
            elif WelkeOpnieuwGooien == 1:
                DobbelSteen1Opnieuw = True
            elif WelkeOpnieuwGooien == 2:
                DobbelSteen2Opnieuw = True
            elif WelkeOpnieuwGooien == 3:
                DobbelSteen3Opnieuw = True
            elif WelkeOpnieuwGooien == 4:
                DobbelSteen4Opnieuw = True
            elif WelkeOpnieuwGooien == 5:
                DobbelSteen5Opnieuw = True
            elif WelkeOpnieuwGooien == 6:
                pass

            else:
                SorrySnapIkNiet()
        return DobbelSteen1Opnieuw and DobbelSteen2Opnieuw and DobbelSteen3Opnieuw and DobbelSteen4Opnieuw and DobbelSteen5Opnieuw

    else:
        SorrySnapIkNiet()
# WilOpnieuwDobbelen()
DobbelStenenVervangen(WilOpnieuwDobbelen())


        # def OpnieuGooienFunctie():
        #     for i in range (1,6):
        #         Dobbel1Opnieuw = input ("Wilt u dobbelsteen " + str(i) + " opnieuw gooien? ")
#         Dobbel1Opnieuw = input ("Wilt u dobbelsteen 1 opnieuw gooien? ")
#         Dobbel2Opnieuw = input ("Wilt u dobbelsteen 2 opnieuw gooien? ")
#         Dobbel3Opnieuw = input ("Wilt u dobbelsteen 3 opnieuw gooien? ")
#         Dobbel4Opnieuw = input ("Wilt u dobbelsteen 4 opnieuw gooien? ")
#         Dobbel5Opnieuw = input ("Wilt u dobbelsteen 5 opnieuw gooien? ")
#     OpnieuwGooien += 1
# PuntenRonde = DobbelSteen1 + DobbelSteen2 + DobbelSteen3 + DobbelSteen4 + DobbelSteen5
# print ("Je totale punten deze ronden zijn:",PuntenRonde)

# GegooideDobbelStenenList = []
# GegooideDobbelStenenList.append(DobbelSteen1)
# GegooideDobbelStenenList.append(DobbelSteen2)
# GegooideDobbelStenenList.append(DobbelSteen3)
# GegooideDobbelStenenList.append(DobbelSteen4)
# GegooideDobbelStenenList.append(DobbelSteen5)

# GegooideDobbelStenenList.sort()

# GegooideDobbelStenen = {

# }
# GegooideDobbelStenen["DobbelSteen 1"] = DobbelSteen1
# GegooideDobbelStenen["DobbelSteen 2"] = DobbelSteen2
# GegooideDobbelStenen["DobbelSteen 3"] = DobbelSteen3
# GegooideDobbelStenen["DobbelSteen 4"] = DobbelSteen4
# GegooideDobbelStenen["DobbelSteen 5"] = DobbelSteen5

# print (GegooideDobbelStenenList)
# print (GegooideDobbelStenen)

# Three of a kind: drie dobbelstenen met dezelfde punten
# if DobbelSteen1 ==  DobbelSteen2 == DobbelSteen3:
#     print ("Je hebt Three of a kind")

# Four of a  kind: vier dobbelstenen met dezelfde punten
# if DobbelSteen1 == DobbelSteen2 == DobbelSteen3 == DobbelSteen4:
#     print ("Je hebt een Four of a kind")
# Full House: 25 punten voor 3 gelijke en een paar (5 gelijke telt niet als full house tenzij het vak Yahtzee reeds is ingevuld.)
# if DobbelSteen1 == DobbelSteen2 == DobbelSteen3 and DobbelSteen4 == DobbelSteen5:
#     print ("Je hebt een Full House")
# Small straight 0 punten voor vier oplopende dobbelstenen(volgorde maakt niet uit)
# if GegooideDobbelStenen == "1,2,3,4" or "2,3,4,5" or "3,4,5,6":
#     print ("Je hebt Small Straight")

# Large straight 40 punten voor 5 oplopende dobbelstenen (Volgorde maakt niet uit)
# if GegooideDobbelStenen == "1,2,3,4,5" or "5,4,3,2,1":
#     print ("Je hebt een Large Straight")
# Yahtzee (top score) 50 punten 50 punten als alle dobbelsten gelijk zijn
# if DobbelSteen1 == DobbelSteen2 == DobbelSteen3 == DobbelSteen4 == DobbelSteen5:
#     print ("Je hebt Yahtzee")

# Chance: totaal aantal punten van alle gegooiden dobbelstenen.