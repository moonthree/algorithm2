arr = [4, 7, 1, 8]

sum = arr[0]

def abc(level):
    global sum
    if level == 3:
        print(sum)
        return
    sum += arr[level+1]
    abc(level+1)
    sum -= arr[level+1]
    print(sum)

abc(0)

print()

def abcd(level, sum2):
    if level == 3:
        print(sum2)
        return
    abcd(level+1, sum2+arr[level+1])
    print(sum2)
abcd(0, arr[0])