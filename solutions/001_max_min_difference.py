"""
SWEA 12384

Original title: 배열1_Min_Max_확인용
Topic: Max-min difference
"""

T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
 
    max_v = ai[0]
    min_v = ai[0]
    for i in range(N):
        if max_v < ai[i]:
            max_v = ai[i]
        if min_v > ai[i]:
            min_v = ai[i]
 
    print(f'#{test_case} {max_v - min_v}')
