def nth_root(x, n=2):
    if n <= 0:
        raise ValueError("Степень n должна быть положительным числом.")
    return x ** (1 / n)
x = int(input())

print(nth_root(x))
