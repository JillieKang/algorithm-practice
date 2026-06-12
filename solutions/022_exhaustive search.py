"""
SWEA 11802

Original title: 완전탐색_최소합
Topic: Exhaustive search
"""

# memoization
# d라는 배열을 생성
# (0,0)에서부터 거기까지 오는 길의 합을 d에 저장
# d[r][c] = min(d[r-1][c], d[r][c-1]) + arr[r][c]임을 이용
# r-1이 없는 경우, c-1이 없는 경우를 고려하자
 
t = int(input())
 
def find_min(r, c):
    up = left = float('inf')
 
    if d[r][c] != float('inf'):
        return d[r][c]
 
    # 기저사례: 재귀호출을 멈출 곳
    if r == 0 and c == 0:
        d[0][0] = arr[0][0]
        return d[0][0]
 
    # 내 왼쪽의 값을 구하자
    if c > 0:
        left = find_min(r, c-1)
 
    # 내 위쪽의 값을 구하자
    if r > 0:
        up = find_min(r-1, c)

    d[r][c] = min(up, left) + arr[r][c]
    return d[r][c]
 
 
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d = [[float('inf')] * n for _ in range(n)] 
  
    ans = find_min(n-1, n-1)
  
    print(f'#{tc} {ans}')
