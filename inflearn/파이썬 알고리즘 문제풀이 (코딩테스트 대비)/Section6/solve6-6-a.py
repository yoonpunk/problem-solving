import sys
sys.stdin = open('in5.txt', 'r')

N, M = list(map(int, input().split()))
num_list = [num for num in range(1, N+1)]

print(num_list)

result_list = []
result_size = 0

def dfs(i):
    global result_size
    if len(result_list) == M:
        result_size += 1
        for num in result_list:
            print(num, end=" ")
        print()
        return
    
    for j in range(0, N):
        result_list.append(num_list[j])
        dfs(j)
        result_list.pop()

dfs(0)
print(result_size)