contacts = {}
try:
    with open("contacts.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            contacts[parts[0]] = parts[1]
except FileNotFoundError:
    pass
    

print("1 - добавить, 2 - найти, 3 - показать все, 4 - выход")
while True:
    x = int(input("Выбери:"))
    if x == 1:
        name = input("Имя:") 
        number = input("Номер:")
        contacts[name] = number
        with open("contacts.txt", "a", encoding="utf-8") as f:
            f.write(f"{name},{number}\n")
        print("Добавлено!")
    elif x == 3:
        print("--- Все контакты: ---")
        for contact in contacts:
            print(contact, "-", contacts[contact])
    elif x == 2:
        sear = input("Чьё имя ищем?")
        if sear in contacts:
            print("Номер", contacts[sear])
    elif x == 4:
        break