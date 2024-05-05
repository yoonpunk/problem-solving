import sys
sys.stdin = open('in0.txt', 'r')

N, F = list(map(int, input().split()))
check = [0]*(N+1)
combination = []

for i in range(N):
    combination.append([1] + [-1]*(N-1))

## nCr
def get_combination(n, r):
    if n < 0 or r < 0 or n < r:
        return 0

    if combination[n][r] != -1:
        return combination[n][r]
    
    combination[n][r] = get_combination(n-1, r-1) + get_combination(n-1, r)
    return combination[n][r]

def do_check(nums):
    result = 0
    n = N-1
    for r in range(N):
        result += get_combination(n, r)*nums[r]
    
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

dfs(0, [])

