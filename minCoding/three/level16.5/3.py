nums = list(map(int, input().split()))

arr = [[nums[i+j*3] for i in range(3)] for j in range(2)]

def max_coord(arr):
    max_value = arr[0][0]
    max_point = '(0,0)'
    for y in range(2):
        for x in range(3):
            if arr[y][x] > max_value:
                max_value = arr[y][x]
                max_point = f'({y},{x})'
    return max_point
def min_coord(arr):
    min_value = arr[0][0]
    min_point = '(0,0)'
    for y in range(2):
        for x in range(3):
            if arr[y][x] < min_value:
                min_value = arr[y][x]
                min_point = f'({y},{x})'
    return min_point

print(max_coord(arr))
print(min_coord(arr))