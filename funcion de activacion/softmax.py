import math

def softmax(valores):
    exponenciales = [math.exp(x) for x in valores]
    suma = sum(exponenciales)
    
    return [x / suma for x in exponenciales]


valores = [2, 1, 0]

resultado = softmax(valores)

print(resultado)
print("Suma:", sum(resultado))