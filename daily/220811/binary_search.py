# 바이너리 서치 이진탐색
# 정렬이 되어있는 data에서 타겟값 찾기
n = int(input())
arr = list(map(int, input().split()))
target = int(input())


def binary_search(st, ed, value):
    while (1):
        mid = (st + ed) // 2  # 미드값 찾기
        if arr[mid] == value:  # 찾을경우
            return 1
        elif arr[mid] > value:  # 찾고자 하는 값이 더 작으면
            ed = mid - 1
        elif arr[mid] < value:  # 찾고자 하는 값이 미드값 보다 더 크면
            st = mid + 1
        if st > ed:  # st index와 ed index 가 교차되면... 없는 숫자
            return 0


arr.sort()
ret = binary_search(0, n - 1, target)
if ret:
    print("찾음")
else:
    print("없는숫자")