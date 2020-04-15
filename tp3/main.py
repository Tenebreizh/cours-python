import Caisse as Caisse

caisse = Caisse.Caisse()

caisse.addProduct({"name": "Banane", "price": 4, "quantity": 20})
caisse.addProduct({"name": "Pomme", "price": 2, "quantity": 10})
caisse.addProduct({"name": "Poire", "price": 3, "quantity": 50})

caisse.showResult()
