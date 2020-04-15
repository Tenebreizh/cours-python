def showProducts(products):
    i = 0
    print("ID ", "Nom ", "Prix")
    print("-------------------")

    for product in products.values():
        i += 1
        print(i, " ", product['nom'], " ", product['prix'])

    print("-------------------")

def subTotalHt(price, quantity):
    return price * quantity

def totalHt(subTotalHt, remise):
    return subTotalHt - remise

def totalTtc(totalHt):
    return totalHt + (totalHt * 0.2)


def showResult(subTotalHt, remise, totalHt, totalTtc):
    print()
    print("-----------------")
    print("Sous-total HT = ", subTotalHt, " €")
    if remise > 0:
        print("Remise 5% = ", remise, " €")
    print("Total HT = ", totalHt, " €")
    print("Total TTC = ", totalTtc, " €")
