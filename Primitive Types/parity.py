# Write a program that returns the parity for a binary number
# if the number of 1's are odd, parity is 1, else 0


def parity(x:int)-> int:
    p = 0
    while(x):
        p ^= 1
        x &= (x-1)
    return p
# This is O(k) where k is the number of bits set 
print(parity(10)) # 1010
print(parity(11)) #1011


def parity2(x:int) -> int:
    x ^= x >>32
    x ^= x >>16
    x ^= x >>8
    x ^= x >>4
    x ^= x >>2
    x ^= x >>1
    return x & 0x1

# This approach is O(log(n)) where n is the size of the word ( in this case n = 32)
print(parity2(10)) # 1010
print(parity2(11)) # 1011
