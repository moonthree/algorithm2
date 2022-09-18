arr = []
MAX = int(-21e8)
MIN = int(21e8)
MAX_idx = 0
MIN_idx = 0
def recur(level):
    global arr, MAX, MIN, MAX_idx, MIN_idx
    word = input()
    arr.append(word)

    if level == 3:
        for i in range(len(arr)):
            if MAX < len(arr[i]):
                MAX = len(arr[i])
                MAX_idx = i
            if MIN > len(arr[i]):
                MIN = len(arr[i])
                MIN_idx = i
        print(f'긴문장:{MAX_idx}')
        print(f'짧은문장:{MIN_idx}')
        return
    recur(level+1)

recur(0)