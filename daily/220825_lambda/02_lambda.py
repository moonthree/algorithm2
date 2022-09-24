# 의미
# 익명함수를 지칭하는 용어
# 기본의 함수(명 등)를 선언하고 사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수

# 형식
# lambda 매개변수 : 표현식
# ex ) sum = lambda x : x+1
def Sum(x, y):
    return x + y
print(Sum(10, 20))

sum_lambda = (lambda x, y: x + y)(10, 20)
print(sum_lambda)

a = (lambda x: x+10)(1)
print(a)