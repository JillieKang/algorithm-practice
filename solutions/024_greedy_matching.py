"""
SWEA 11804

Original title: 탐욕_컨테이너 운반
Topic: Greedy matching
"""

# w와 t를 내림차순으로 정렬
# 앞에서부터 t와 w를 비교한 다음
# 만약 t >= w라면, count += w
# 만약 t < w라면, 다음 w와 t를 비교
 
t_c = int(input())
for tc in range(1, t_c+1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)
 
    i = 0
    j = 0
    weight = 0
 
    while i < n and j < m:
        if t[j] >= w[i]:
            weight += w[i]
            i += 1
            j += 1
        else:
            i += 1
 
    print(f'#{tc} {weight}')
