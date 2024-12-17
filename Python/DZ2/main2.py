a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+ - * /): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b == 0:
        result = "На ноль делить нельзя"
    else:
        result = a / b
else:
    result = "Неверная операция"

print("Результат: ", result)
