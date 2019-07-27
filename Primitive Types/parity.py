# Write a program that returns the parity for a binary number
# if the number of 1's are odd, parity is 1, else 0


def parity(x:int)-> int:
    p = 0
    while(x):
        p ^= 1
        x &= (x-1)
    return p

print(parity(10)) # 1010
print(parity(11)) #1011