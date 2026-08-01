mes = int(input("Mes (1-12): "))
if mes in [12, 1, 2]:
    print("Invierno")
elif mes in [3, 4, 5]:
    print("Primavera")
elif mes in [6, 7, 8]:
    print("Verano")
elif mes in [9, 10, 11]:
    print("Otoño")
else:
    print("Mes no válido")
