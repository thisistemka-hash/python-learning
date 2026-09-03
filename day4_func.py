def hello():
    print("Привет, мир!")

hello()

def greet(name):
    print("Здраствуй,", name)

greet("Артём")
greet("Катя")

def square(x):
    return x*x

result = square(5)
print("5 в квадрате =",result)
print("3 в квадрате =", square(3))