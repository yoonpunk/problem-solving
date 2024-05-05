import sys
sys.stdin = open('in5.txt', 'r')

N, F = list(map(int, input().split()))
check = [0]*(N+1)
combination = [1]*N

## nCr
def get_combination():
    for i in range(1, N):
        combination[i] = combination[i-1]*(N-i)/i

def do_check(nums):
    result = 0
    for r in range(N):
        result += combination[r]*nums[r]
    
    if F == result:
        for num in nums:
            print(num, end=' ')
        print()
        exit()

def dfs(n, nums):
    if sum(check) == N:
        do_check(nums)
        return 
    
    for i in range(1, N+1):
        if check[i] == 1:
            continue

        check[i] = 1
        nums.append(i)
        dfs(n+1, nums)

        check[i] = 0
        nums.pop()

get_combination()
dfs(0, [])

