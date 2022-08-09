def isSame(a, b):
    if a == b :
        return 'pass'
    else:
        return 'fail'

min_pw = [3, 7, 4, 9]
new_pw = list(map(int, input().split()))

print(isSame(min_pw, new_pw))