year = int(input())

if (year % 400 == 0):
    print(f"{year} - високосный год.")
elif (year % 100 == 0):
    print(f"{year} - невисокосный год.")
elif (year % 4 == 0):
    print(f"{year} - високосный год.")
else:
    print(f"{year} - невисокосный год.")
