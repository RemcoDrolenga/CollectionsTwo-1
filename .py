import random
OpnieuwGooien = 0
OpnieuwDobbelen = True
Dobbel1Opnieuw = True
Dobbel2Opnieuw = True
Dobbel3Opnieuw = True 
Dobbel4Opnieuw = True
Dobbel5Opnieuw = True
Dobbel6Opnieuw = True

while OpnieuwDobbelen == True and OpnieuwGooien < 3:
    while Dobbel1Opnieuw == True:
        DobbelSteen1 = random.randint(1,6)
        Dobbel1Opnieuw = False 
    while Dobbel2Opnieuw == True:
        DobbelSteen2 = random.randint(1,6)
        Dobeel2Opnieuw = False
    while Dobbel3Opieuw == True:
        DobbelSteen3 = random.randint(1,6)
        Dobbel3Opnieuw = False
    while Dobbel4Opnieuw == True:
        DobbelSteen4 = random.randint(1,6)
        Dobbel4Opnieuw = False
    while Dobbel5Opnieuw == True:
        DobbelSteen5 = random.randint(1,6)
        Dobbel5Opnieuw = False 
    while Dobbel6Opnieuw == True:
        DobbelSteen6 = random.randint(1,6)
        Dobbel6Opnieuw = False   
    print ("Dobbelsteen 1: ",DobbelSteen1 )
    print ("Dobbelsteen 2: ",DobbelSteen2 )
    print ("Dobbelsteen 3: ",DobbelSteen3 )
    print ("Dobbelsteen 4: ",DobbelSteen4 )
    print ("Dobbelsteen 5: ",DobbelSteen5 )
    print ("Dobbelsteen 6: ",DobbelSteen6 )

    WilOpnieuw = input("Wilt u nog een keer gooien J/N ")
    if WilOpnieuw == "N":
        OpnieuwDobbelen = False
    else: 
        WelkeOpnieuw = input ("Welke wilt u opnieuw gooien? ")
        if WelkeOpnieuw == 1:
            Dobbel1Opnieuw = True
        if WelkeOpnieuw == 2:
            Dobbel2Opnieuw = True
    OpnieuwGooien += 1