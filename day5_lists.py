    # создание и доступ
fruits = ["яблоко", "банан", "груша"]
print(fruits[0])
print(fruits[-1])
print("Всего фруктов:", len(fruits))

# изменение
fruits.append("апельсин")
fruits[1] = "манго"
print(fruits)

# перебор циклом
print("--- Список фруктов ---")
for fruit in fruits:
    print("-", fruit)

# сумма чисел через список
numbers = [10, 25, 3, 47]
total = 0
for n in numbers:
    total = total + n
print("Сумма:", total)