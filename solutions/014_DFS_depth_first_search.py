"""
SWEA 12398

Original title: 스택1_그래프_경로
Topic: Depth-first search(DFS)
"""

T = int(input())
 
def dfs(v):
    # dfs(v)를 호출하면
    # 일단 visited[v] = 1
    visited[v] = 1
    # G[v] 속 요소 w들을 순회하며
    for w in G[v]:
        # 만약 visited[w]이 0이면 dfs(w) 호출
        if not visited[w]:
            dfs(w)
 
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 1번부터 V번까지의 빈 리스트 생성
    G = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
 
    for i in range(E):
        # E개의 edge(숫자쌍) 일일이 반복해서 읽기
        u, v = map(int, input().split())
        # 유향 그래프이므로, u --> v만 반영
        G[u].append(v)
 
    # 그 다음 주어진 tart랑 end 좌표 읽기
    start, end = map(int, input().split())
     
    # 주어진 start를 시작점으로 하여 dfs()를 호출
    dfs(start)
 
    # start를 시작으로 호출한 다음
    # 그 결과 visited[end]에 표시가 되었는지 확인
    result = 1
    if visited[end] == 0:
        result = 0
 
    print(f'#{tc} {result}')
