words = input()
a, b = input().split()
words_list = list(words)

a_idx = words.index(a)
b_idx = words.index(b)


if a_idx == 0:
    words_list[a_idx + 1] = '#'
elif a_idx == len(words)-1:
    words_list[a_idx - 1] = '#'
else:
    words_list[a_idx + 1] = '#'
    words_list[a_idx - 1] = '#'

if b_idx == 0:
    words_list[b_idx + 1] = '#'
elif b_idx == len(words)-1:
    words_list[b_idx - 1] = '#'
else:
    words_list[b_idx + 1] = '#'
    words_list[b_idx - 1] = '#'

for i in words_list:
    print(i, end='')