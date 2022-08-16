words = input()
idx = int(input())

words_list = [i for i in words]
words_list.pop(idx)

for i in words_list:
    print(i, end='')