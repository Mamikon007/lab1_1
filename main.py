a = int(input("Напиши первое число: "))
b = int(input("Напиши второе число: "))

a1 = a
b1 = b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

result = a + b
print(f"НОД({a1}, {b1}) = {result}")
