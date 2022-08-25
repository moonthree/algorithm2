arr = list(input())
n = int(input())

arr.sort(reverse=True)
z = ord('Z')
bucket = [0]*(z+1)

for i in range(n):
    bucket[ord(arr[i])] += 1

maxi = max(bucket)

for i in range(len(bucket)):
    if maxi == bucket[i]:
        print(chr(i))
        break


