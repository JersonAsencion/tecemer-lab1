def escalon(x):
    if x >= 0:
        return 1
    else:
        return 0

valores = [-3, -1, 0, 1, 3]

for x in valores:
    print(f"f({x}) = {escalon(x)}")