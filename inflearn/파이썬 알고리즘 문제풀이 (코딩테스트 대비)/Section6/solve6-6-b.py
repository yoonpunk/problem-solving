import sys
sys.stdin = open('in5.txt', 'r')

N, M = list(map(int, input().split()))
result_list = [0 for _ in range(0, N)]
result_count = 0

def dfs(l):
    global result_count

    if l == M:
        for index in range(0, M):
            print(result_list[index], end=" ")
        print()
        result_count += 1
        return

    for i in range(1, N+1):
        result_list[l] = i
        dfs(l+1)

dfs(0)
print(result_count)