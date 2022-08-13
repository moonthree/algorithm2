words = input()

words_50 = words[0:len(words)//2]

words_100 = words[len(words)//2:len(words)]

if words_50 == words_100:
    print('동일한문장')
else:
    print('다른문장')