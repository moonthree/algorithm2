vect = [3, 5, 4, 2, 6, 6, 5]

bit = list(map(int, input().split()))

for i in range(len(vect)):
    if bit[i] == 0:
        vect[i] = 0

for i in range(len(vect)):
    if bit[i] != 0:
        vect[i] = 7

for i in vect:
    print(i, end='')