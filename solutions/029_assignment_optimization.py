"""
SWEA 1865

Original title: 동철이의 일 분배
Topic: Backtracking with pruning (assignment optimization)
"""

# backtracking
# 행 별로 몇 번 열의 요소를 고를 건지 결정
# 이미 방문표시 된 열의 요소는 고를 수 없음
# 현재 성공확률을 계속 넘겨주면서, 최대 성공확률보다 작아졌다면 pruning
# 기저조건: 모든 행에 대해 선택 완료, 최대 성공확률인지 검사
 
# depth: 행의 개수
# branch: 열의 개수

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_prob = -float('inf')
    visited = [0] * n
 
    def recur(row, now_prob):
        global max_prob
 
        if now_prob <= max_prob:    # pruning
            return
 
        if row == n:    # 기저조건
            max_prob = max(now_prob, max_prob)
            return
 
        for col in range(n):
            if visited[col] == 1:
                continue
            visited[col] = 1
            recur(row + 1, now_prob * arr[row][col] / 100)
            visited[col] = 0
 
    recur(0, 1) # 확률이니 초기값은 1
 
    print(f'#{tc} {max_prob*100:.6f}')
