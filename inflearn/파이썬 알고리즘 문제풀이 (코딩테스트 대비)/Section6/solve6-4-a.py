import sys
sys.stdin = open('in5.txt', "r")

N = int(input())
number_list = list(map(int, input().split()))

left = []
right = []

def dfs(i):
    if i >= N:
        if sum(left) == sum(right):
            print("YES")
            sys.exit()
        return
    
    left.append(number_list[i])
    dfs(i+1)
    left.pop()

    right.append(number_list[i])
    dfs(i+1)
    right.pop()

dfs(0)
print("NO")
