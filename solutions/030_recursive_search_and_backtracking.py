"""
SWEA 11896

Original title: 백트래킹_전기버스2
Topic: Backtracking and Recursive search
"""

# 정류장 1에서 선택할 수 있는 경우의 수는 2가지[2, 3]
# 이 때 2,3 이라는 범위는 충전지의 숫자로 결정
# 정류장 i번에서, 배터리 j라면, 최대 i + j까지 갈 수 있음
 
# 이 방법을 통해 가능한 모든 방법을 탐색
# n까지 도착했을 때 최소 횟수를 업데이트
# 현재 선택횟수를 재귀호출마다 계속 넘겨주면서, 이것이 저장된 최소 횟수를 넘어서면 pruning

t = int(input())
for tc in range(1, t+1):
    lst = list(map(int, input().split()))
    n = lst[0]  # 5 = 출발점부터 종점까지 갯수
    stop_lst = lst[1:]  # 출발점부터 종점 - 1까지 배터리 양 정보
    min_time = float('inf')
 
 
    def recur(stop, times):
        global min_time
 
        if min_time <= times: # pruning
            return
 
        if stop >= n-1:  # 기저조건: 종점에 도착했으면 끝. 종점은 3번
            min_time = min(min_time, times)
            return
 
        # 시작점(0번)에서 선택할 수 있는 경우의 수 = 1번, 2번
 
        for i in range(1, stop_lst[stop] + 1):
            recur(stop + i, times + 1)
 
    recur(0, 0)
  
    print(f'#{tc} {min_time - 1}')
