class Caisse:
    def __init__(self):
        self.subTotalHt = 0.0
        self.remise = 0.0
        self.totalHt = 0.0
        self.totalTtc = 0.0
        self.products = []

    # ajout produit (prix * quantité) à la caisse
    def addProduct(self, product):
        self.subTotalHt += float(product['price']) * float(product['quantity'])
        self.products.append(product)
        print(self.products)

    def calculRemise(self):
        if self.subTotalHt > 200:
            self.remise = self.subTotalHt * 0.05
            return self.remise

    def calculTotalHt(self):
        self.totalHt = self.subTotalHt - self.remise
        return self.totalHt

    def calculTotalTtc(self):
        self.totalTtc = self.totalHt + (self.totalHt * 0.2)
        return self.totalHt

    def showResult(self):
        self.calculRemise()
        self.calculTotalHt()
        self.calculTotalTtc()

        print("+-----------+------------+---------------+---------------+")
        print("|    Nom    |    Prix    |   Quantité    |   Total HT    |")
        print("+-----------+------------+---------------+---------------+")
        for product in self.products:
            # print(product)
            print("|  ", product["name"], " |     ", product["price"], "     |    ", int(product["quantity"]), "     | ", float(product["price"]) * product["quantity"], "         |")
        print("+-----------+------------+---------------+---------------+")
        print()
        print("Sous-total HT = ", self.subTotalHt, " €")
        if self.remise:
            print("Remise 5% = ", self.remise, " €")
        print("Total HT = ", self.totalHt, " €")
        print("Total TTC = ", self.totalTtc, " €")
