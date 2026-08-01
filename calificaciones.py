parcial = float(input("Parcial (0-100): "))
proyecto = float(input("Proyecto (0-100): "))
examen = float(input("Examen (0-100): "))

if not (0 <= parcial <= 100 and 0 <= proyecto <= 100 and 0 <= examen <= 100):
    print("Error: notas fuera de rango")
else:
    final = parcial*0.4 + proyecto*0.3 + examen*0.3
    print(f"Calificación final: {final:.2f}")
    if final >= 60:
        print("Aprobado")
    else:
        print("Reprobado")
