import sys
sys.stdin = open('in5.txt', 'r')

N, K = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
result_count = 0

def dfs(l, idx, summation):
    global result_count

    if l == K:
        if summation % M == 0:
            result_count += 1
        return
    
    for i in range(idx, N):
        dfs(l+1, i+1, summation+nums[i])


dfs(0, 0, 0)
print(result_count)