a = input()
b = input()


# 자를 단어
def abc(a, b):
    for i in range(len(b) - 1, -1, -1):
        for j in range(len(b) - i):
            k = b[j:j + i + 1]
            if a.find(k) != -1:
                return k


print(abc(a, b))
