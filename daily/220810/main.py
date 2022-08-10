import sys
sys.stdin = open("input.txt", "r")

'''
# 입력파일에 저장할 값
hello
45
1 2 3
3.14
1.2 2.3 3.4
one two three
1 2 45 43
1234
4
1011
1001
0001
1000
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

# 1.문자열 입력 받기
# st = 'hello'

st = input()
print(st)

# 2.정수형 변수 입력 받기
# N = 45
# A, B, C = 1, 2, 3

N: int = int(input())
A, B, C = map(int, input().split())
print(N)
print(A, B, C)

# 3.실수형 변수 입력 받기
# F = 3.14
# A, B, C = 1.2, 2.3, 3.4
F = float(input())
A, B, C = map(float, input().split())
print(F)
print(A, B, C)


# 4.한 줄에 있는 공백으로 구분된 단어들을 각각 문자열로 리스트에 저장하기
# lst = ['one', 'two', 'three']
lst = list(map(str, input().split()))
print(lst)


# 5.한 줄에 있는 공백으로 구분된 숫자들을 각각 숫자로 리스트에 저장하기
# lst = [1, 2, 45, 43]
lst = list(map(int, input().split()))
print(lst)

# 6.한 줄에 있는 공백없는 한자리 숫자들을 각각 숫자로 리스트에 저장하기
# lst = [1, 2, 3, 4]
#a = str(input())
#lst = [int(i) for i in a]
lst2 = list(map(int, input()))
#print(lst)
print(lst2)


# 7.2차원 (N*N) 공백없는 한자리 숫자들을 2차원 arr에 저장
# 4
# 1011
# 1001
# 0001
# 1000
N = int(input())
arr = []
for _ in range(N):
    a = str(input())
    arr.append([int(i) for i in a])
print(arr)

# 8.2차원 (N*N) 정수값을 2차원 arr에 저장 (N값과 arr값)
# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)


# 9.(입력은 아니지만) 0값 10개를 가진 1차원 lst 생성
# lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
lst = [0]*10
print(lst)

# 10.(입력은 아니지만) 0값 3 * 3 개를 가진 2차원 arr생성
# arr = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
arr = [[0]*3 for _ in range(3)]
print(arr)

print('End')
