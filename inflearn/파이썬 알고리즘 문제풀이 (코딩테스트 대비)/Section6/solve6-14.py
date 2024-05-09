import sys
sys.stdin = open('in1.txt', 'r')

N, M = list(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(N):
    matrix.append([0]*N)

for _ in range(M):
    x, y, w = list(map(int, sys.stdin.readline().split()))
    matrix[x-1][y-1] = w

for x in range(N):
    for y in range(N):
        print(matrix[x][y], end=' ')
    print()