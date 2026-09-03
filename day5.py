tovars=[]
while True:
    x=input("Что купить? (стоп для завершения):")
    if x=="стоп":
        break
    tovars.append(x)
print("--- Список покупок ---")
for tovar in tovars:
    print("-", tovar)

print("Всего товаров:", len(tovars))