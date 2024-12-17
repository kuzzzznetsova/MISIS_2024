def are_numbers_unique(numbers):
    return len(numbers) == len(set(numbers))

numbers = [1, 4, 5]
result = are_numbers_unique(numbers)

if result:
    print("Все числа уникальны.")
else:
    print("Есть повторяющиеся числа.")
