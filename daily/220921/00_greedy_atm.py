n = int(input())

arr = list(map(int, input().split()))

arr.sort()
answer = 0
for i in range(1, len(arr)+1):
    for j in range(0, i):
        answer += arr[j]

print(answer)


# n=int(input())
# time_w=list(map(int,input().split()))
#
# time_w.sort(reverse=True)
#
# answer=0
# for i in range(1,n+1):
#     answer+=(i*time_w[i-1])
# print(time_w)
# print(answer)