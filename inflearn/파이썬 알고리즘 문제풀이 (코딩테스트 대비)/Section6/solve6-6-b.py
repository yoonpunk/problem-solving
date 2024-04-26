import sys
sys.stdin = open('in4.txt', 'r')

C, N = list(map(int, input().split()))
dog_list = [int(input()) for _ in range(N)]

total_sum = sum(dog_list)
max_result = -2147000000

def dfs(i, summation):
    global max_result

    if summation > C:
        return

    if i >= N:
        if summation > max_result:
            max_result = summation
        return
    
    remained_summation = sum(dog_list[i:])
    if max_result > summation + remained_summation:
        return

    dfs(i+1, summation+dog_list[i])
    dfs(i+1, summation)

dfs(0, 0)
print(max_result)