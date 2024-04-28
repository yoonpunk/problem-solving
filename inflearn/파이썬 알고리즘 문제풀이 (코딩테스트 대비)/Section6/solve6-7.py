import sys
sys.stdin = open('in2.txt', 'r')

N = int(input())
coin_list = list(map(int, input().split()))
remained = int(input())
coin_list.sort(reverse=True)
coin_sum = 0
count = 0
result_count = 2147000000


def dfs(l):
    global coin_sum
    global count
    global result_count

    if coin_sum > remained:
        return
    
    if coin_sum == remained:
        if result_count > count:
            result_count = count
        return
    
    if count >= result_count:
        return

    for i in range(0, N):
        coin_sum += coin_list[i]
        count += 1
        dfs(l+1)
        coin_sum -= coin_list[i]
        count -= 1

dfs(0)
print(result_count)