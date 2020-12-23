n = int(input())
a = 0
print(a)
b = 1
print(b)
c = 0
for i in range (0,n):
    c = a + b
    a = b
    b = c
    print(c)