dia = int(input("Día (1-7): "))
dias = ["", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
if 1 <= dia <= 7:
    print(dias[dia])
else:
    print("Día no válido")
