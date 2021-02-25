#Imprima un triángulo invertido de la siguiente forma que depende de la altura.


triangle = lambda n: '\n'.join([
    f"{' ' * (n - i - 1)}{'*' * (2 * i + 1)}"
    for i in range(n - 1, -1, -1)
])

#Imprimir las figuras con alturas 1, 2 y 3
print(triangle(4)+'\n')
print(triangle(5)+'\n')
print(triangle(6)+'\n')