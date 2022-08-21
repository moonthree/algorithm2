n = input()

for i in range(ord(n), ord(n)+3):
    for j in range(3):
        for k in range(3):
            print(chr(i), end='')
        print()
    print()

