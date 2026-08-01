compra = float(input("Total de compra: "))
if compra >= 1000:
    desc = compra * 0.20
elif compra >= 500:
    desc = compra * 0.10
else:
    desc = 0
print(f"Descuento: ${desc:.2f}")
print(f"Total a pagar: ${compra-desc:.2f}")
