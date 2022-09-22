# 최대공약수
# 숫자 2개 입력받고
# 최대 공약수를 구하겠다. -> 2부터 둘 중 작은 수 까지 나누었을 때
# 나눠지는 수 중 가장 큰 수

# 32 16 -> 16
# 24 16 -> 8

# 최대 공약수 구하기 1
# a, b = map(int, input().split())
# answer = 0
# for i in range(2, min(a,b)+1):
#     if a%i == 0 and b%i == 0:
#         answer = i
# print(answer)

# 최대공약수를 조금 더 빠르게 구하기 = 유클리드 호제법(최초의 알고리즘)
c, d = map(int, input().split())
def gcd(c, d):
    while d > 0:
        c, d = d, c % d
    return c

# 최소공배수 구하기
def lcm(c, d):
    return c * d / gcd(c, d)
print('최대공약수 : ',gcd(c, d))
print('최소공배수 : ',lcm(c, d))
