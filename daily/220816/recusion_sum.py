arr = [3, 4, 5, 1, 6, 9]
#sum을 전역변수로 놓은 경우
sum = 3
def abc(level):
    global sum
    print(sum)
    if level == 5:
        return
    sum += arr[level+1]
    abc(level+1)
abc(0)
# sum을 매개변수로 놓은 경우
# def abc(level, sum):
#     print(sum)
#     if level == 5:
#         return
#     abc(level+1, sum+arr[level+1])
# abc(0, 3)