# Write a program that multiply two nonnegative integers using only assignment, bitwise operators and boolean checks

# The idea here is the same as primitive multiplication we learn in school
# Remember how to multiply 12x10?

#   12
#  x10
#    0
# +12     <--- this is like a shift in the decimal number
# =120


# Now multiplying it in binary would result the same
#
#                1100
#               x1010
#                0000   
#               1100
#              0000
#             1100
#            =1111000
def multiply(x: int, y: int):
    
    result = 0
    def add(a, b):
        while(b):
            c = a & b # c here is the carry out 1&1 = 1, 0 otherwise
            a = a ^ b # 0 if a and b are equal, 1 otherwise
            b = c << 1
        return a

    while(x):
        if(x&1):
            result = add(result, y)
        x >>= 1
        y <<= 1
    return result

print(multiply(10,12))