
#Calcule la siguiente función utilizando su ecuación de recurrencia, donde n y m son naturales (incluye el 0).
cache = {}

def equation(n: int, m: int):
    if f'{n,m}' in cache:
        return cache[f'{n,m}']

    result = 1;
    if m==n:
        return 1

    if m==0:
        return 1

    result = cache[f'{n,m}'] = equation(n-1, m) + equation(n-1, m-1)
    return result


print(equation(50,35))
print(equation(100,85))