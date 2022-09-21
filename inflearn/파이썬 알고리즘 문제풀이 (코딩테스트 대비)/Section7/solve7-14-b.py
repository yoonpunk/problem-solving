from collections import deque
import sys
sys.stdin = open('in1.txt', 'r')

## bfs 풀이

# 지도 탐색을 위한 bfs, 안전지역을 탐색하며 visit_map에 방문정보를 남김
def bfs(y, x, height):

    qu = deque()
    qu.append([y, x])
    visit_map[y][x] = 1

    while qu:

        curr_pos = qu.popleft()
        for i in range(4):

            next_y = curr_pos[0] + dy[i]
            next_x = curr_pos[1] + dx[i]

            # 다음 방문 지역 체크 로직
            # 1. 지도 안에 존재하는 좌표
            # 2. 침수되지 않는 좌표 (map_[next_y][next_x]>height)
            # 3. 방문한 적이 없는 좌표 (visit_map[next_y][next_x]==0)
            if 0 <= next_y and next_y < N and 0 <= next_x and next_x < N and map_[next_y][next_x] > height and visit_map[next_y][next_x] == 0:
                visit_map[next_y][next_x] = 1
                qu.append([next_y, next_x])


if __name__ == '__main__':

    # 상하좌우 좌표 탐색을 위한 변화값
    dx = [0, 0, -1, +1]
    dy = [-1, +1, 0, 0]

    # 초기값 설정
    N = int(input())
    map_ = []        # 지도 정보 공간
    visit_map = []   # 방문 정보 공간
    curr_count = 1   # 현재 안전지역 갯수
    result = 1       # 결과값
    heights = set()  # 각 지역의 높이 정보 저장 공간

    # 지도 정보 입력 및 각 지역의 높이 정보 저장
    for i in range(N):
        map_.append(list(map(int, input().split())))
        heights.update(map_[i])
    
    # 각 지역의 높이만큼 비가 올 수 있으므로 모든 지역의 높이를 순회하며 bfs 수행
    for height in heights:

        # 매 침수 사건마다 방문 정보 공간 초기화
        visit_map = []
        for i in range(N):
            visit_map.append([0] * N)

        # 모든 좌표 순회하며 bfs 시작
        # 침수지역이 아닌 곳, 방문하지 않은 곳에서만 bfs 시작
        curr_count = 1
        for i in range(N):
            for j in range(N):
                if map_[i][j] > height and visit_map[i][j] == 0:
                    curr_count += 1
                    bfs(i, j, height)

        # 결과값 최신화
        if result < curr_count:
            result = curr_count
    
    # 결과 리턴
    print(result)