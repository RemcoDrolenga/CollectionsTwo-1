OpnieuwVragen = True
BoodSchappenLijstje = {

}
while OpnieuwVragen == True:
    LijstjeToevoegen = input("Wat wilt u toevoegen aan het boodschappenlijstje? ")
    HoeveelToevoegen = int(input("Hoeveel " + LijstjeToevoegen +" wilt u toevoegen aan het lijstje? "))
    BoodSchappenLijstje.update({LijstjeToevoegen: HoeveelToevoegen})
    OpnieuwToevoegen = input("Wilt u nog meer toevoegen aan uw lijstje? ")
    if OpnieuwToevoegen == "nee":
        OpnieuwVragen = False

print (BoodSchappenLijstje)