# tree

# 트리의 순회 (탐색하면서 출력)
# preorder  전위순회
# postorder 후위순회
# inorder   중위순회

arr = ' ABCDEFG'

def preorder(now):
    if now > len(arr)-1:
        return
    print(arr[now], end=' ')
    preorder(now * 2)
    preorder(now * 2 + 1)

preorder(1)
# len(arr) = 8
# if now > 7: return

# preorder(1)

# 1 > 7
# arr[1] = A
# preorder(2), preorder(3)

# 2 > 7, 3 > 7
# arr[2] = B, arr[3] = C
# preorder[4], preorder[5], preorder[6], preorder[7]

# 4 > 7, 5 > 7, 6 > 7, 7 > 7
# arr[4] = D



# def postorder(now):
#     if now > len(arr)-1:
#         return
#     postorder(now * 2)
#     postorder(now * 2 + 1)
#     print(arr[now], end=' ')
#
# def inorder(now):
#     if now > len(arr)-1:
#         return
#     inorder(now * 2)
#     print(arr[now], end=' ')
#     inorder(now * 2 + 1)

# print()
# postorder(1)
# print()
# inorder(1)

