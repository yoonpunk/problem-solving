import sys
sys.stdin = open('in4.txt', 'r')
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N+1):
    graph.append([0]*(N+1))

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1

result = 0
check = [0] * (N+1)

def dfs(node):
    global result

    if node == N:
        result +=1
        return

    next_list = graph[node]
    for i in range(1, N+1):
        if check[i] == 0 and next_list[i] == 1:
            check[i] = 1
            dfs(i)
            check[i] = 0
            
check[1] = 1
dfs(1)
print(result)