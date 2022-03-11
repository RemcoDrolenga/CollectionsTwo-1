# Bekijk de officiele spelregels van UNO.
# Begin met de vraag voor het aantal spelers.
# Alle spelers worden bestuurd door het programma.
# Een programma gestuurde speler:
# kiest altijd de hoogst mogelijke kaart om te spelen
# kiest altijd de kleur waar het de meeste kaarten van heeft (mits mogelijk)
# Zorg dat je bijhoud wat er in de stapels en ieder zijn/haar handen zitten.
# Laat zien wat iedereen speelt en wat de bovenste open kaart is.
# Laat aan het einde de score en winnaar zien.
OpnieuwVragen = True
while OpnieuwVragen == True:
    HoeveelSpelers = int(input("Met hoeveel spelers moet er gespeeld worden? "))
    GetalCheck = HoeveelSpelers.isdigit()
    if GetalCheck == True:
        if HoeveelSpelers >= 2 and HoeveelSpelers <= 10:
            OpnieuwVragen = False
        else:
            print ("Je moet met minimaal 2 spelers zijn en maximaal met 10. ")
    else:
        print ("Je kan alleen maar getallen invullen. ")
def KaartenMaken():
    GetallenLijst = [1,2,3,4,5,6,7,8,9]