arr = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]

startIndex = int(input())

def getSum(idx):

    sum = 0
    for i in range(idx, idx+5):
        sum += arr[i]
    return sum

print(getSum(startIndex))