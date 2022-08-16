stra = [input() for _ in range(4)]

def words(level):
    # 인덱스 위치는 레벨값
    if level == 4:
        return
    words(level+1)

words(0)