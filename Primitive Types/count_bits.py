# Count the number of bits that are set in a number


def count_bits(n:int) -> int:
    count = 0
    while(n):
        count += n&1
        n >>=1

    return count

print(count_bits(10))