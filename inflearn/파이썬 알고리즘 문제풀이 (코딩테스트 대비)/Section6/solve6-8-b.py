import sys
sys.stdin = open('in5.txt', 'r')

N, M = list(map(int, input().split()))

check = [0] * (N+1)
result = [0] * M
count = 0

def dfs(l):
    global count

    if l == M:
        for num in result:
            print(num, end=' ')
        print()
        count += 1
        return
    
    for num in range(1, N+1):
        if check[num] == 1:
            continue

        result[l] = num
        check[num] = 1
        dfs(l+1)
        check[num] = 0

dfs(0)
print(count)