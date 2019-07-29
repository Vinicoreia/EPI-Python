# Write a program that takes an array A and an index i into A and
# rearranges the elements such that all elements less than A[i] appear first
# followed by elements equal to the pivot, followed by elements greater than the pivot

from typing import List


def dutch_flag_partition(A:List[int], x: int) -> List[int]:
    pivot = A[x]
    # one idea is to establish 3 abstract partitions
    # the first one are numbers less than the pivot
    # second are numbers equal to the pivot
    # the third are numbers greater than the pivot

    less = 0
    equal = 0
    greater = len(A)-1

    while(equal < greater):
        if(A[equal] < pivot):
            A[less], A[equal] = A[equal], A[less]
            less += 1
            equal += 1
        elif(A[equal] == pivot):
            equal += 1
        else:
            A[equal], A[greater] = A[greater], A[equal]
            greater -= 1
    return A



print(dutch_flag_partition([0,0,0,2,2,2,1,2,1,2,0,0,1], 6))