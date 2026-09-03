try:
    age = int(input("Сколько тебе лет?"))
    print(f"Через год тебе будет {age + 10}")
except ValueError:
    print("Ошибка: нужно ввести число!")

try:
    a = int(input("Делимое: "))
    b = int(input("Делитель: "))
    print(f"{a} / {b} = {a / b}")
except ValueError:
    print("Нужно вводить числа")
except ZeroDivisionError:
    print("На ноль делать нельзя!")