list1 = [1, 2, 4]
list2 = [4, 5, 6]

set_difference = set(list1) - set(list2)
list_difference = list(set_difference)

print(list_difference)

def DobbelSteenOpnieuwGooien(VerwijderDobbelSteenList, DobbelStenenList):
    VerwijderdeDobbel = VerwijderDobbelSteenList.remove(1)
    print (VerwijderDobbelSteenList)
    DobbelStenenList.remove(VerwijderdeDobbel)
    DobbelSteen = random.randint(1,6)
    DobbelStenenList.append(DobbelSteen)
    return DobbelStenenList