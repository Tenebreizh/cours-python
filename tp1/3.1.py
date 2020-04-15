# 3.1
price_ht = float(input("Prix hors taxe: "))
quantity = float(input("Quantité: "))

price = price_ht + (price_ht * 0.2)
total = price * quantity

if total > 200:
    total -= total * 0.05

print ("Le total est de", total)