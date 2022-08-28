n=int(input())
result=[]
# n보다 작은 수가 2번째에 와야함 
# 2번째 수까지 li에 넣기
for i in range(n):
    li = []
    li.append(n)
    li.append(i)
# 넣어진 리스트에서 뒤에서 2번째와 1번째의 차가 0보다작으면 그만 돌리기
    while 1:
        if li[-2]-li[-1]<0:
            break
        else:
            li.append(li[-2]-li[-1])
# 만들어진 리스트를 새리스트에 넣기
    result.append(li)
# 다 넣어진 result리스트를 각 for 문 돌아가면서 1~100까지 2번째 숫자 가 된 리스트의 길이를 카운트하여 구하기
a=sorted(result, key=lambda x:-len(x))
print(len(a[0]))
print(*a[0])