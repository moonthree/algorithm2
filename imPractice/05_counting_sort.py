a = [4, 7, 1, 3, 4, 1, 2, 4]
n = int(input())
b = list(map(int, input().split()))

# b리스트의 값이 a 리스트 안에 각각 몇개 존재 출력
bucket = [0]*10
# a의 값을 버켓에 등록
for i in range(len(a)):
    bucket[a[i]] += 1
    #index=a[i]
    #bucket[index]+=1
for i in range(len(b)):
    print(f'{b[i]}: {bucket[b[i]]}개 존재')