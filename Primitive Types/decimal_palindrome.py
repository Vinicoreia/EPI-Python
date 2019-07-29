# Check if a decimal number is a palindrome number

#Ex:
# input: 212
# output: true

# input: -212
# output: false
import math


def is_number_palindrome(x:int) -> bool:
    # how do i take the first number in a binary number?
    # we can get the first number by simply doing 
    # number divided by the 10 to the number of digits -1
    # to findout how many digits a number n has you can take it's 
    # n_digits = floor(log10(n)) + 1
    # example:
    # n = 315 and n has 3 digits, this means to get the 3 we just divided 
    # 315 // 100 == 3
    # To get the last digit we already know that we just have to take it's module by 10
    # 315 % 10 == 5

    if(x<0):
        return False
    elif(x<10):
        return True

    number_digits = 10**(math.floor(math.log10(x))) 
    
    while(number_digits > 0 and x // number_digits == (x % 10)):
        x%=number_digits # This extracts the first number
        x //= 10
        number_digits /= 100
    return False if(x>9) else True

print(is_number_palindrome(312))
print(is_number_palindrome(1))
print(is_number_palindrome(11))
print(is_number_palindrome(2222))
print(is_number_palindrome(-121))
print(is_number_palindrome(33314))