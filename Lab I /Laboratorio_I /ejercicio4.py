

'''
Obtenido  de stackoverflow https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
'''
#: Imprima un lista de los números primos menores a 100000 en un segundo.

def primes_list(n):

    primes_list = set(range(2, n + 1, 1))
    primes_list.difference_update(set(range(0, n + 1, 2)))
    primes = [1]

    while primes_list:
        eval = primes_list.pop()
        primes.append(eval)
        primes_list.difference_update(set(range(eval * 2, n + 1, eval)))

    return primes

#primes_list(100000)
#print(primes_list(100000))