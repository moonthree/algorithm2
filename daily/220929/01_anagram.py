a = input()
b = input()
flag = 0
if sorted(a) == sorted(b):
    print('anagram')
else:
    print('no anagram')
