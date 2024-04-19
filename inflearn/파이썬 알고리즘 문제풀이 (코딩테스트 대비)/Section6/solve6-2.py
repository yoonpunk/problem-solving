## 이진트리 전위, 중위, 후위 순회
# 전위순회
def preorder_dfs(n):
    if n>7:
        return
    
    print(n, end=" ")
    preorder_dfs(n*2)
    preorder_dfs(n*2 + 1)

# 중위순회
def inorder_dfs(n):
    if n>7:
        return
    
    inorder_dfs(n*2)
    print(n, end=" ")
    inorder_dfs(n*2 + 1)


# 후위순회
def postorder_dfs(n):
    if n>7:
        return
    
    postorder_dfs(n*2)
    postorder_dfs(n*2 + 1)
    print(n, end=" ")

## 순회
print("전위순회")
preorder_dfs(1)

print(" ")
print("중위순회")
inorder_dfs(1)

print(" ")
print("후위순회")
postorder_dfs(1)