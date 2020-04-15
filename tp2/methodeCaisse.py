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


def showResult(selectedProducts, subTotalHt, remise, totalHt, totalTtc):
    print(selectedProducts)
    print("+-----------+------------+---------------+---------------+")
    print("|    Nom    |    Prix    |   Quantité    |   Total HT    |")
    print("+-----------+------------+---------------+---------------+")
    for product in selectedProducts:
        # print(product)
        print("|  ", product[0], " |     ", product[1], "     |    ", int(product[2]), "     | ", float(product[1]) * product[2], "         |")
    print("+-----------+------------+---------------+---------------+")
    print()
    print("Sous-total HT = ", subTotalHt, " €")
    if remise > 0:
        print("Remise 5% = ", remise, " €")
    print("Total HT = ", totalHt, " €")
    print("Total TTC = ", totalTtc, " €")
