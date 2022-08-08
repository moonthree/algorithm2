word = input()
idx = int(input())

word_list = [i for i in word]
word_list.insert(idx, 'A')

for i in word_list:
    print(i, end='')