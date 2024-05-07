import sys
sys.stdin = open('in5.txt', 'r')

N, K = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
result_count = 0

result = [0]*K

def check(curr_nums):
    if sum(curr_nums) % M == 0:
        return True
    
    return False

def dfs(l, idx):
    global result_count

    if l == K:
        if check(result):
            result_count += 1
        return

    for i in range(idx, N):
        result[l] = nums[i]
        dfs(l+1, i+1)

dfs(0, 0)
print(result_count)