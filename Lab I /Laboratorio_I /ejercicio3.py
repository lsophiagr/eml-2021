#Imprima un rombo de la siguiente forma que depende de la altura.
import math

diamante = lambda n: '\n'.join([
    f"{' ' * ((n-i)-1)} {'* ' * (i+1)}" if i<math.ceil(n/2) else f"{' ' * (i)} {'* ' * (n-i)}"
    for i in range(n)
])

print(diamante(7)+"\n")
print(diamante(9)+"\n")
print(diamante(11)+"\n")