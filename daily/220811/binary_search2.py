battery = "***_______"

def parametric_search(st, ed):
    MAX = -1
    while(1):
        mid = (st+ed)//2
        if battery[mid]=='_':
            ed = mid-1
        elif battery[mid] == '*':
            MAX = mid
            st = mid+1
        if st > ed:
            break
    return MAX+1

answer = parametric_search(0, 9)
print(answer*10)
