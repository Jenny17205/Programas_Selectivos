a = float(input("Num 1: "))
b = float(input("Num 2: "))
c = float(input("Num 3: "))
if a >= b and a >= c:
    print(f"Mayor: {a}")
elif b >= a and b >= c:
    print(f"Mayor: {b}")
else:
    print(f"Mayor: {c}")
