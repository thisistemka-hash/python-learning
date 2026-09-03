with open("shopping.txt", "w", encoding="utf-8") as f:
    f.write("молоко\n")
    f.write("хлеб\n")

with open("shopping.txt", "a", encoding="utf-8") as f:
    f.write("яйца\n")

print("--- Список товаров ---")
with open("shopping.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("-", line.strip())

try:
    with open("net_takogo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Такого файла нет!")