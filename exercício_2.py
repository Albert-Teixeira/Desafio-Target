def fibonacci(n):
    if 0<=n<=2:
        return "sim"
    else:
        a, b = 0, 1
        while b<n:
            a, b = b, a + b
        if b == n:
            return "sim"
        else:
            return "não"

numero = int(input())
print(fibonacci(numero))
