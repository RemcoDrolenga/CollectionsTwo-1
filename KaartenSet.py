import random
Doorgaan = True

KleurKaarten = ["Schoppen", "Harten", "Ruiten", "Klaver"]
KaartWaardes = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Boer", "Vrouw", "Heer", "Aas"]
KaartenDeck = set()
def KaartenKiezen(KaartDeck):
    for i in range (52):
        KleurKiezen = random.choice(KleurKaarten)
        WaardeKiezen = random.choice(KaartWaardes)
        KaartenDeck.add(KleurKiezen + str(WaardeKiezen))
    return KaartDeck
KaartenKiezen(KaartenDeck)

while Doorgaan == True:
    if len(KaartenDeck) == 52:
        Doorgaan = False
    else:
        KaartenKiezen(KaartenDeck)
    

KaartenDeckList = list(KaartenDeck)
random.shuffle(KaartenDeckList)

for i in range (2):
    KaartenDeckList.append('Joker')


KaartenDeckList = list(KaartenDeck)
random.shuffle(KaartenDeckList)


for i in range(1,8):
    KaartWeghalen = KaartenDeckList[i]
    print ("Kaart", str(i) + ":",KaartenDeckList[i])
    KaartenDeck.remove(KaartWeghalen)
print ("")
print (KaartenDeck)
