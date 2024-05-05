import sys
from collections import deque
sys.stdin = open('in5.txt', 'r')

N, M = map(int, input().split())

def dfs(nums):
    if len(nums) == N:
        if check(nums):
            for num in nums:
                print(num, end=' ')
            exit()
        return
    
    for num in range(1, N+1):
        if num in nums:
            continue

        nums.append(num)
        dfs(nums)
        nums.pop()

def check(nums):
    curr_line = nums.copy()
    while(len(curr_line) >= 2):
        curr_line = line_up(curr_line)
    
    if curr_line[0] == M:
        return True
    else:
        return False


def line_up(nums):
    new_line = []
    if len(nums) == 2:
        return [nums[0] + nums[1]]
    
    for i in range(len(nums)-1):
        left = nums[i]
        right = nums[i+1]
        new_line.append(left+right)
    return new_line

dfs([])