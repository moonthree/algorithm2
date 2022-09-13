def bbq(a):
    global arr
    if a == 4:
        arr.append(a)
        return
    arr.append(a)
    bbq(a+1)
    arr.append(a)

arr = []
bbq(0)
print(arr)