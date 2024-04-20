import sys
sys.stdin = open("in4.txt", "r")

N = int(input())

def dfs(number, number_list):
    if number > N:
        for num in number_list:
            print(num, end=" ")
        print(" ")
        return
    
    number_list.append(number)
    dfs(number+1, number_list)

    number_list.pop()
    dfs(number+1, number_list)

dfs(1, list())