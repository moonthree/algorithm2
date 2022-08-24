p = int(input())
n = int(input())

for i in range(n):
    p = p*2
    p2 = str(p)
    p3 = p2[::-1]
    p = int(p3)

print(p)
