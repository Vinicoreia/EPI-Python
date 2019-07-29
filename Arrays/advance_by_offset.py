
# Suppose you have an array like [3,3,1,0,2,0,1]
# every number in the array is the number of steps you can give towards the end of the array
# Write a program that returns True if the end can be reached and false if you can not reach the end

# In the array of the example [3,3,1,0,2,0,1] you can reach the end by
# move 1 to index 1, move 3 to index 4, move 2 to index 6 and move 1 to the end
# you can take 3 steps but you don't necessarily have to do so.

from typing import List

def advance_by_offset(A:List[int]) -> bool:
    howFar = 0
    i = 0

    for i in range(len(A)):
        if(i>howFar or howFar>=len(A)):
            break
        howFar = max(howFar, A[i]+i)        
    return howFar >= len(A)


print(advance_by_offset([3,3,1,0,2,0,1]));
print(advance_by_offset([3,3,1,0,0,0,1]));
print(advance_by_offset([0,3,1,0,2,0,1]));
print(advance_by_offset([10,3,1,0,2,0,1]));