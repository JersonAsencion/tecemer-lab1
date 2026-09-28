import numpy as np

def gelu(x):
    return 0.5 * x * (
        1 + np.tanh(
            np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)
        )
    )

valores = [-2, -1, 0, 1, 2]

for x in valores:
    print(f"GELU({x}) = {gelu(x):.4f}")