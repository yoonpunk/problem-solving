import sys
sys.stdin = open("in5.txt", "r")

N = int(input())
NUM_LIST = list(map(int, input().split()))
TOTAL = sum(NUM_LIST)

def dfs(i, summation):
    if summation > TOTAL/2:
        return 
    
    if i >= N:
        return

    if summation == TOTAL-summation:
        print("YES")
        sys.exit()

    dfs(i+1, summation+NUM_LIST[i])
    dfs(i+1, summation)

dfs(0, 0)
print("NO")
