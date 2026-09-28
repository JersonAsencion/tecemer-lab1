# Función de activación lineal
def funcion_lineal(x):
    return x

# Valores de entrada
valores = [-5, -2, -1, 0, 1, 2, 5]

# Aplicamos la función
for x in valores:
    y = funcion_lineal(x)
    print(f"Entrada: {x:>3}  ->  Salida: {y:>3}")