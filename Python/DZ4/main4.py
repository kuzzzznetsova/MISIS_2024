def sum_of_digits(n):
    n = abs(n)
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum
def sum(n):
    sum = 0
    while n > 0:
        a = n % 10
        sum = sum + a
        n = n//10
    return sum

n = int(input())
print(int(sum(n)))
