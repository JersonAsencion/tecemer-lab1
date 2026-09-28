import math

def tanh(x):
    return math.tanh(x)

valores = [-5, -2, -1, 0, 1, 2, 5]

for x in valores:
    y = tanh(x)
    print(f"Entrada: {x:>3} → Salida: {y:.4f}")