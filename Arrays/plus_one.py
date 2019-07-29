# Given an integer splitted in its digits in an array
# 130 = [1,3,0]
# increment it by one and return the result.
from typing import List


def plus_one(A:List[int]) -> List[int]:
    
    A[-1] += 1

    if(A[-1]!= 10):
        return A
    else:
        i = len(A) - 1
        while(A[i] == 10):
            if(i == 0):
                break
            else:
                A[i] = 0
                A[i-1] += 1
            i -= 1
    if(A[0] == 10):
        A.append(0)
        A[0] = 1
    return A


print(plus_one([9]))
print(plus_one([9,9]))
print(plus_one([1,4,5]))
print(plus_one([0]))