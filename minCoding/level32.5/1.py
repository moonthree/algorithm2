arr = ['ABCD', 'ABCE', 'AGEH', 'EIEI', 'FEQE', 'ABAD']

search = input()
search_arr= []
for i in range(len(search)):
    if search[i] != '?':
        search_arr.append([i, search[i]])

cnt = 0
for word in arr:
    cnt2 = 0
    for j in range(len(search_arr)):
        for k in range(4):
            if search_arr[j][0] == k and search_arr[j][1] == word[k]:
                cnt2 += 1
        if cnt2 == len(search_arr):
            cnt += 1

print(cnt)