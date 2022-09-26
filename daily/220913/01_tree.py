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

def postorder(now):
    if now > len(arr)-1:
        return
    postorder(now * 2)
    postorder(now * 2 + 1)
    print(arr[now], end=' ')

def inorder(now):
    if now > len(arr)-1:
        return
    inorder(now * 2)
    print(arr[now], end=' ')
    inorder(now * 2 + 1)

# print()
# postorder(1)
# print()
# inorder(1)

