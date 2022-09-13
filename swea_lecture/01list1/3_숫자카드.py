t = int(input())

for tc in range(1, t+1):
    n = int(input())
    num = list(input())

    bucket = [0]*10
    maxi = int(-21e8)
    maxi_num = 0

    for i in range(len(num)):
        bucket[int(num[i])] += 1

    for i in range(len(bucket)):
        if bucket[i] >= maxi_num:
            maxi = i
            maxi_num = bucket[i]

    print(bucket)
    print(maxi)
    print(maxi_num)
