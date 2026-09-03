print("--- for ---")
for i in range(1, 6):
    print("Проход номер", i)

print("--- накопление ---")
total = 0
for i in range(1, 6):
    total= total + i
print("Сумма от 1 до 5", total)

print("--- while ---")
count = 0
while count < 3:
    print("count=", count)
    count = count + 1
print("Цикл закончен")