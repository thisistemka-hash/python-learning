
d = int(input("Первое число:"))
c = int(input("Второе число:"))

def suma(x, y):
    return x+y


def minus(x, y):
    return x-y


def umno(x, y):
    return x*y


def dele(x, y):
    return x/y



print(d, "+", c, "=", suma(d, c))
print(d, "-", c, "=", minus(d, c))
print(d, "*", c, "=", umno(d, c))
print(d, "/", c, "=", dele(d, c))