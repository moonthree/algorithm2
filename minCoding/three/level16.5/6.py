words = input()

words_list = [ord(i) for i in words]

def max_idx(arr):
    return arr.index(max(arr))
def min_idx(arr):
    return arr.index(min(arr))

print(max_idx(words_list))
print(min_idx(words_list))
