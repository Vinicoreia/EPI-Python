# Compute all prime numbers up to N

from typing import List

def primes(n:int)-> List[int]:
    if(n<= 2):
        return [2]
    
    sieve = [True] * n
    i = 0
    prime = []
    for i in range(2, n):
        if(sieve[i] == True):
            prime.append(i)
            for j in range(i*2, n, i):
                sieve[j] = False
    return prime


print(primes(200))