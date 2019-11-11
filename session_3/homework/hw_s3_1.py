n = int(input("Input your number: "))

# Tinh giai thua cua n:


def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        f = x * factorial(x-1)
        return f


print(factorial(n))

# Tinh so Fibonaci thu n trong day:


def fibonaci(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        s = fibonaci(x-2) + fibonaci(x-1)
        return s


print(fibonaci(n))

# In ra dong thu n cua tam giac Pascal:


def pascalbase(x):
    base = [1]
    if x == 2:
        base.append(1)
    elif x > 2:
        for i in range(1, x-1):
            base.append(pascalbase(x-1)[i] + pascalbase(x-1)[i-1])
        base.append(1)
    return base


print(pascalbase(n))
