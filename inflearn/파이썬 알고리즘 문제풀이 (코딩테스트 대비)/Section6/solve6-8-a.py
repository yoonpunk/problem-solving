import sys
sys.stdin = open('in5.txt', 'r')

N, M = list(map(int, input().split()))
result_count = 0

def dfs(result):
    global result_count

    if len(result) == M:
        for num in result:
            print(num, end=' ')
        print()
        result_count += 1
        return

    for num in range(1, N+1):
        if num in result:
            continue

        result.append(num)
        dfs(result)
        result.pop()

dfs([])
print(result_count)