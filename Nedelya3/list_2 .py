a = int(input("Введите число"))

def fib(n):
    a,b = 1, 0
    for i in range(n):
        yield a
        a,b = b, a + b
        


print(list(fib(a)))
