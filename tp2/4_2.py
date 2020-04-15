#4.2
import methodeCaisse as caisse

products = {
    1: {
        'nom': "Banane",
        "prix": 4
    },
    2: {
        'nom': "Pomme",
        "prix": 2
    },
    3: {
        'nom': "Orange",
        "prix": 1.5
    },
    4: {
        'nom': "Poire",
        "prix": 3
    }
}

# Affichage des produits disponibles
caisse.showProducts(products)

subTotalHt = 0
remise = 0
totalHt = 0
total = 0
print("Tapez 0 pour finir la selection")
print("--------------------------------")

while(True):
    # Selection de l'article
    try:
        selectedItem = int(input("Quel article voulez-vous ? (Utiliser l'ID) "))

        # Verification de l'article choisi (si 0, arrêt de la selection)
        if selectedItem == 0:
            break
        else:
            print("Vous avez selectionné : ", products[selectedItem]['nom'])
        product = products[selectedItem]
    except ValueError:
        print("Vous devez indiquer un chiffre !")
        break
    except KeyError:
        print("Cet article n'existe pas !")
        break


    # Selection de la quantité d'article
    quantity = float(input("Quantité: "))

    productPrice = float(product['prix'])

    # Sous-total HT
    subTotalHt += caisse.subTotalHt(productPrice, quantity)

if subTotalHt > 200:
    remise += subTotalHt * 0.05

# Total HT
totalHt = caisse.totalHt(subTotalHt, remise)

# Total TTC
totalTtc = caisse.totalTtc(totalHt)

# Affichage résultat
caisse.showResult(subTotalHt, remise, totalHt, totalTtc)