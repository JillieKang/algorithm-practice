"""
SWEA 11652

Original title: 큐_미로의거리_확인용
Topic: Breadth-first search
"""

# 최단 거리 또는 0을 출력
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
 
def dfs(r, c):
    # 만약 지금 조사중인 거리가 전에 조사된 d[er][ec]보다 크면
    # 탐색 중단
    if d[r][c] >= d[er][ec]: 
        return
 
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 델타: 인덱스 유효성 검사 필수
        # 만약 유효하지 않은 인덱스라면
        # 다음 방향 탐색으로 넘어가기
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
          
        # 만약 maze[nr][nc]이 벽이 아니면서
        # 이번에 새로 탐색해서 찾은 거리 d[r][c]+1 또한
        # 기존 d[nr][nc]의 값보다 더 작다면  
        if maze[nr][nc] != 1 and d[nr][nc] > d[r][c] + 1:
            # d[r][c]에 1 더함
            d[nr][nc] = d[r][c] + 1
 
            dfs(nr, nc)
            # g[nr][nc]로 들어가서 해당 좌표에서 탐색 시작
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    # 시작점 좌표 sr sc, 출구 좌표 er ec
    sr = sc = er = ec = 0
    # 미로의 크기 (n x n)
    for i in range(n):
        for j in range(n):  
            # 2차원 배열 전체 탐색해서 2와 3 찾기
            if maze[i][j] == 2:
                sr, sc = i, j
            if maze[i][j] == 3:
                er, ec = i, j
 
    d = [[float('inf')] * n for _ in range(n)]
    # 시작점의 거리(d)는 0
    d[sr][sc] = 0 
 
    dfs(sr, sc)
  
    # 탐색 실패시 0을 출력
    ans = 0

    # 만약 d[er][ec]가 초기값에서 다른 값으로 업데이트 되었다면 출력
    if d[er][ec] != float('inf'):
        # 단 도착점은 거리에서 제외
        ans = d[er][ec] - 1 
 
    print(f'#{tc} {ans}')
