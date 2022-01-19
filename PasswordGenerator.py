import random
KleineLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
GroteLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
SpecialeTekens = ["@","#","$","%","&","_","?"]
Cijfers = ["0","1","2","3","4","5","6","7","8","9"]
TekenToevoegen = random.choice(KleineLetters)
Wachtwoord = TekenToevoegen

AantalGroteLetters = random.randint(2,6)
AantalCijfers = random.randint(4,7)
AantalKleineLetters = 20 - AantalGroteLetters - AantalCijfers

#Grote letters toevoegen
for i in range (AantalGroteLetters):
    TekenToevoegen = random.choice(GroteLetters)
    Wachtwoord += TekenToevoegen

#Speciale Tekens toevoegen
for i in range (3):
    SpeciaalTekenToevoegen = random.choice(SpecialeTekens)
    Wachtwoord += SpeciaalTekenToevoegen

#Cijfers Toevoegen
for i in range (AantalCijfers):
    CijferToevoegen = random.choice(Cijfers)
    Wachtwoord += CijferToevoegen

#Kleine Letters Toevoegen
for i in range (AantalKleineLetters):
    KleineLetterToevoegen = random.choice(KleineLetters)
    Wachtwoord += KleineLetterToevoegen

print (Wachtwoord)