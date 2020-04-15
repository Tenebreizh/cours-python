# 3.2
products = int(input("Nombre de produits: "))
total = 0

for i in range(0, products):
    print("--------------------------------------")
    price_ht = float(input("Prix hors taxe: "))
    quantity = float(input("Quantité: "))

    price = price_ht + (price_ht * 0.2)
    subtotal = price * quantity

    if subtotal > 200:
        subtotal -= subtotal * 0.05
    total += subtotal

print ("Le total est de", total)
