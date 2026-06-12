"""
SWEA 11805

Original title: 탐욕_화물_도크
Topic: Interval scheduling
"""

# 종료시간이 빠른 것부터 정렬
# (다음 스케쥴 시작시간) >= 이전 종료시간이면, cnt += 1
# 이전 종료시간 = arr[i][1]로 업데이트 한 다음 
# 다음 턴으로 넘어감
 
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])
 
    end = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i][0] >= end:
            cnt += 1
            end = arr[i][1]
 
    print(f'#{tc} {cnt}')
