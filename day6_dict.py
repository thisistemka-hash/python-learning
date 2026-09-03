prices = {"молоко": 80, "хлеб": 40, "яйца": 120}

print("Молоко стоит:", prices["молоко"])

prices["сыр"] = 200
prices["хлеб"] = 45
print(prices)

if "сыр" in prices:
    print("Сыр есть, цена:", prices["сыр"])

print("--- Прайс-лист ---")
for product in prices:
    print(product, "-", prices[product])

print("Всего товаров:", len(prices))