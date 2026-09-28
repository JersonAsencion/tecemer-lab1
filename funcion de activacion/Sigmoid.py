import math

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

valores = [-5, -2, -1, 0, 1, 2, 5]

for x in valores:
    y = sigmoide(x)
    print(f"Entrada: {x:>3} → Salida: {y:.4f}")