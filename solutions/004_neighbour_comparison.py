"""
SWEA 1206

Original title: View
Topic: Neighbor comparison
"""

T = 10
 
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    view_num = 0
    for i in range(2, N-2):    # 시작점에도 1의 여유 필요
        tempo_max = arr[i-2]    # 일단 맨 왼쪽 건물이 제일 높다 가정
 
        if tempo_max < arr[i - 1]:
            tempo_max = arr[i - 1]
        if tempo_max < arr[i + 1]:
            tempo_max = arr[i + 1]
        if tempo_max < arr[i + 2]:
            tempo_max = arr[i + 2]
 
        if arr[i] > tempo_max:
            view_num += (arr[i] - tempo_max)
 
    print(f'#{test_case} {view_num}')
