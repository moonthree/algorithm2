arr = list(map(int, input().split()))
arr.sort()
answer = 0
while len(arr) != 1:
    answer += arr.pop(0)*len(arr)

print(answer)
