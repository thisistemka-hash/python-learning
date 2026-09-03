contacts = {}
print("1 - добавить, 2 - найти, 3 - показать все, 4 - выход")
while True:
    x = int(input("Выбери:"))
    if x == 1:
        name = input("Имя:") 
        contacts[name] = input("Номер:")
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