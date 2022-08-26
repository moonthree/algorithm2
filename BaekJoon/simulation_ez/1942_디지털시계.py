

for _ in range(3):
    st, ed = input().split()

    st1, st2, st3 = st.split(':')
    ed1, ed2, ed3 = ed.split(':')

    start = int(st1)*60*60 + int(st2)*60 + int(st3)
    end = int(ed1)*60*60 + int(ed2)*60 + int(ed3)


    cnt = 0
    if end > start:
        for i in range(start, end+1):
            if i%3 == 0:
                cnt += 1
    else:
        start2 = (23-int(st1))*60*60 + (59-int(st2))*60 + (59-int(st3))
        for i in range(start2+end):
            if i % 3 == 0:
                cnt += 1
    print(cnt)
