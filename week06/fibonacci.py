def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b  # I am using tuple unpacking to set two variables on one line of code
        L.append(a)
    return L
print(fibonacci(10))