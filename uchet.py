rashods= {}
try:
    with open("rashods.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            if parts[0] in rashods:
                     rashods[parts[0]] = rashods[parts[0]] + int(parts[1])
            else:
                     rashods[parts[0]] = int(parts[1])
except FileNotFoundError:
    pass

print("1 - Добавить расход, 2 - Показать все, 3 - Итого, 4 - Выход")
while True:
    x = int(input("Выбери:"))
    if x == 1:
        name = input("Категория:") 
        price = int(input("Цена:"))
        if name in rashods:
                rashods[name] = rashods[name] + price
        else:
                rashods[name] = price
        with open("rashods.txt", "a", encoding="utf-8") as f:
            f.write(f"{name},{price}\n")
        print("Добавлено!")
    elif x == 2:
        print("--- Все категории: ---")
        for rashod in rashods:
            print(rashod, "-", rashods[rashod])
    elif x == 3:
        total = 0
        for rashod in rashods:
            total = total + rashods[rashod]
        print(f"Итого: {total}")
    elif x == 4:
        break