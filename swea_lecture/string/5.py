import sys
sys.stdin = open("GNS_test_input.txt", "r")

arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())

for tc in range(t):
    a, b = input().split()
    input_arr = list(map(str, input().split()))

    print(a)
    for i in arr:
        num = input_arr.count(i)
        for j in range(num):
            print(i, end=' ')
    print()