n = int(input())

evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]

def conan(start):

    if evid[start] == -1:
        return
    conan(evid[start])
    print(f'{start}번index({timeStamp[start]}시)')

print('0번index(출발)')
conan(n)