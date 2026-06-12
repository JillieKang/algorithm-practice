"""
SWEA 23795

Original title: 우주 괴물
Topic: Simulation
"""

t = int(input())
 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    # 먼저 괴물의 위치 파악
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                mon = [i, j]
 
    # 괴물의 위치로부터 새로운 좌표를 생성
    # 해당 방향으로 1칸 ~ n-1칸까지 활용 가능
    for d in range(4):
        for dis in range(1, n):
            ni = mon[0] + di[d] * dis
            nj = mon[1] + dj[d] * dis
            # 델타는 항상 인덱스 유효성 검사
            if not (0 <= ni < n and 0 <= nj < n):
                break
            if arr[ni][nj] == 1:
                break
            if arr[ni][nj] == 0:
                arr[ni][nj] = 3
 
    # 빔을 다 칠했다면
    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                result += 1
 
    print(f'#{tc} {result}')
