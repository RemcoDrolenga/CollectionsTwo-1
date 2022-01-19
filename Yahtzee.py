import random
Dobbel1Opnieuw = "ja"
Dobbel2Opnieuw = "ja"
Dobbel3Opnieuw = "ja"
Dobbel4Opnieuw = "ja"
Dobbel5Opnieuw = "ja"
OpnieuwGooien = 1
OpnieuwDobbelen = True
while OpnieuwDobbelen == True and OpnieuwGooien < 4:
    if Dobbel1Opnieuw == "ja":
        DobbelSteen1 = random.randint(1,6)
    if Dobbel2Opnieuw == "ja":
        DobbelSteen2 = random.randint(1,6)
    if Dobbel3Opnieuw == "ja":
        DobbelSteen3 = random.randint(1,6)
    if Dobbel4Opnieuw == "ja":
        DobbelSteen4 = random.randint(1,6)
    if Dobbel5Opnieuw == "ja":
        DobbelSteen5 = random.randint(1,6)
    print ("Dobbelsteen 1: ",DobbelSteen1 )
    print ("Dobbelsteen 2: ",DobbelSteen2 )
    print ("Dobbelsteen 3: ",DobbelSteen3 )
    print ("Dobbelsteen 4: ",DobbelSteen4 )
    print ("Dobbelsteen 5: ",DobbelSteen5 )
    Dobbel1Opnieuw = "nee"
    Dobbel2Opnieuw = "nee"
    Dobbel3Opnieuw = "nee"
    Dobbel4Opnieuw = "nee"
    Dobbel5Opnieuw = "nee"

    WilOpnieuw = input("Wilt u nog een keer gooien ")
    if WilOpnieuw == "nee":
        OpnieuwDobbelen = False
    else: 
        Dobbel1Opnieuw = input ("Wilt u dobbelsteen 1 opnieuw gooien? ")
        Dobbel2Opnieuw = input ("Wilt u dobbelsteen 2 opnieuw gooien? ")
        Dobbel3Opnieuw = input ("Wilt u dobbelsteen 3 opnieuw gooien? ")
        Dobbel4Opnieuw = input ("Wilt u dobbelsteen 4 opnieuw gooien? ")
        Dobbel5Opnieuw = input ("Wilt u dobbelsteen 5 opnieuw gooien? ")
    OpnieuwGooien += 1
PuntenRonde = DobbelSteen1 + DobbelSteen2 + DobbelSteen3 + DobbelSteen4 + DobbelSteen5
print ("Je totale punten deze ronden zijn:",PuntenRonde)

GegooideDobbelStenen = []
GegooideDobbelStenen.append(DobbelSteen1)
GegooideDobbelStenen.append(DobbelSteen2)
GegooideDobbelStenen.append(DobbelSteen3)
GegooideDobbelStenen.append(DobbelSteen4)
GegooideDobbelStenen.append(DobbelSteen5)

GegooideDobbelStenen.sort()

print (GegooideDobbelStenen)

if GegooideDobbelStenen == "1,2,3,4" or "2,3,4,5" or "3,4,5,6":
    print ("Je hebt Small Straight")
if DobbelSteen1 == DobbelSteen2 == DobbelSteen3 == DobbelSteen4 == DobbelSteen5:
    print ("Je hebt Yahtzee")

# Three of a kind: drie dobbelstenen met dezelfde punten
# Four of a  kind: vier dobbelstenen met dezelfde punten
# Full House: 25 punten voor 3 gelijke en een paar (5 gelijke telt niet als full house tenzij het vak Yahtzee reeds is ingevuld.)
# Small straight 0 punten voor vier oplopende dobbelstenen(volgorde maakt niet uit)
# Large straight 40 punten voor 5 oplopende dobbelstenen (Volgorde maakt niet uit)
# Yahtzee (top score) 50 punten 50 punten als alle dobbelsten gelijk zijn
# Chance: totaal aantal punten van alle gegooiden dobbelstenen.