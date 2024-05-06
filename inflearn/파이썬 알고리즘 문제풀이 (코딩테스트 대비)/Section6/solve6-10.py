import sys
sys.stdin = open('in5.txt', 'r')

N, M = list(map(int, input().split()))
nums = [0]*(N+1)
result_count = 0

def dfs(n, idx):
    global result_count

    if n == M:
        for i in range(1, N+1):
            if nums[i] == 1:
                print(i, end=' ')
        result_count += 1
        print()
        return
    
    for i in range(idx+1, N+1):
        nums[i] = 1
        dfs(n+1, i)
        nums[i] = 0

dfs(0, 0)
print(result_count)