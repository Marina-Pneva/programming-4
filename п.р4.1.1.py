def Fibanacci(n):
    if n < 2:
        return n
    else:
        return Fibanacci(n - 1) + Fibanacci(n - 2)


n = int(input())
for i in range(n):
    print(Fibanacci(i))
