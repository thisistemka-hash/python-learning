try:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    try:
        print(f"{a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
except ValueError:
    print("Дурак, зачем введ буквы!")
