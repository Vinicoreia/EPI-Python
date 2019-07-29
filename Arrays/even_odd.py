# use two pointers to classify an array between even, odd and unclassified
from typing import List


def even_odd(A: List[int]) -> List[int]:
    even = 0
    odd = len(A) - 1

    while(even<odd):
        if(A[even] % 2 == 1):
            A[even], A[odd] = A[odd], A[even]
            odd -= 1
        else:
            even += 1

    return A

print(even_odd([x for x in range(10)]))