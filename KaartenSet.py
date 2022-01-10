import random

KleurKaarten = ["Schoppen", "Harten", "Ruiten", "Klaver"]
KaartWaardes = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Boer", "Vrouw", "Heer", "Aas"]
KaartenDeck = []
for i in range (54):
    KleurKiezen = random.choice(KleurKaarten)
    WaardeKiezen = random.choice(KaartWaardes)
    KaartenDeck.append(KleurKiezen + str(WaardeKiezen)) 
for i in range (2):
    KaartenDeck.append('Joker')
random.shuffle(KaartenDeck)
for i in range(7):
    KaartWeghalen = KaartenDeck[i]
    print (KaartenDeck[i])
    KaartenDeck.remove(KaartWeghalen)
print ("")
print (KaartenDeck)
