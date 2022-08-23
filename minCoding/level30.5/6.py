def dfs(level, word, password):
    global count

    if word == password:
        print(count+1)
        return

    if level == len(word):
        count += 1
        # print(f'word = {word} / password = {password}')
        return

    for i in range(26):
        word[level] = chr(ord(word[level]) + i)
        dfs(level+1, word, password)
        word[level] = chr(ord(word[level]) - i)


n = int(input())
words = [input() for _ in range(n)]
alpha = [chr(ord('A') + i) for i in range(26)]

for word in words:
    count = 0
    dfs(0, ['A', 'A', 'A', 'A'], list(word))


# def recur(level, word):
#     global flag
#     global cnt
#     if flag == 1:
#         return
#     if level == 4:
#         cnt += 1
#         recur_words = ''
#         for i in range(level):
#             recur_words += path[i]
#         if recur_words == word:
#             flag = 1
#             print(cnt)
#         return
#     for i in range(len(spell)):
#         path[level] = spell[i]
#         recur(level+1, word)
#
# n = int(input())
# st = ord('A')
# ed = ord('Z')
# spell = []
# for i in range(st, ed+1):
#     spell.append(chr(i))
#
# arr = []
# for _ in range(n):
#     arr.append(input())
# path = ['']*4
#
#
# cnt = 0
# for i in range(len(arr)):
#     flag = 0
#     recur(0, arr[i])
#     cnt = 0
