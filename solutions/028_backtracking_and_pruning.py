"""
SWEA 11897

Original title: 백트래킹_최소 생산 비용
Topic: Backtracking with pruning
"""

# backtracking
# 모든 행을 탐색하면서, 각 행마다 어느 열의 요소를 고를지 결정
# 만약 이미 방문했던 열이라면 선택할 수 없음
# 최소합을 계속 업데이트
# 만약 이미 그 합이 최소합을 넘었다면, 그 방향으로의 탐색은 중단

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = float('inf')
    visited = [0] * n
    factories = []
 
    def recur(row, now_sum):
        global min_sum
 
        if now_sum >= min_sum:  # pruning: 탐색 더 하지 말기
            return
 
        if row == n:    # 기저조건: 모든 행 다 선택 완료
            min_sum = min(min_sum, now_sum)
            return
 
        for col in range(n):    # 한 행에 대해 모든 열의 요소를 다 조회
            if visited[col]:
                continue
 
            visited[col] = 1
            recur(row + 1, now_sum + arr[row][col])
            visited[col] = 0
 
    recur(0, 0)
  
    print(f'#{tc} {min_sum}')
