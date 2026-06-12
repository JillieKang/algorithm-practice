"""
SWEA 11620

Original title: 스택2_미로_확인용
Topic: Depth-first search
"""

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
 
def maze_run(n, maze):
    s = []
    visited = [[0] * n for _ in range(n)]
    # 시작좌표 설정
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_i = i
                start_j = j
    # 시작좌표를 push
    visited[start_i][start_j] = 1
    s.append((start_i, start_j))
    # s가 비어있지 않을 때까지 계속
    while s:
        i, j = s.pop()
        # 새 인덱스 생성
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            # 새 인덱스의 유효성 검사
            if 0 <= ni < n and 0 <= nj < n:
                # 3을 만나면
                if maze[ni][nj] == 3:
                    return 1
                # 0을 만나면
                if maze[ni][nj] != 1 and visited[ni][nj] != 1:
                    visited[ni][nj] = 1
                    s.append((ni, nj))
    else:
        return 0
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    result = maze_run(n, maze)
  
    print(f'#{tc} {result}')
