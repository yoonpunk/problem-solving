## 시간 초과
import sys
sys.stdin = open('in0.txt', 'r')

C, N = list(map(int, input().split()))
dog_list = [int(input()) for _ in range(N)]

max_weight = 0
total_weight = 0

def dfs(i):
    global total_weight
    global max_weight

    if i >= N:
        if C >= total_weight and total_weight > max_weight:
            max_weight = total_weight
        return 
    
    if total_weight > C:
        return
    
    total_weight += dog_list[i]
    dfs(i+1)

    total_weight -= dog_list[i]
    dfs(i+1)

dfs(0)
print(max_weight)