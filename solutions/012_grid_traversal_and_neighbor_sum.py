"""
SWEA 16268

Original title: 풍선팡2
Topic: Grid traversal and neighbor sum
"""

T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
 
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
 
    # 상하좌우 합의 최대값 탐색
    max_v = 0
 
    # i는 1번부터 n-2번까지
    for i in range(N):
        # j는 1번부터 m-2번까지
        for j in range(M):
            # ij마다 상하좌우 합 구하기
            sum_v = A[i][j]
            # ij에 대해 새로운 인덱스 만들기
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                # 새로운 인덱스가 유효한지 검사
                if 0 <= ni < N and 0 <= nj < M:
                    sum_v += A[ni][nj]
            # sum 값 완성한 뒤에
            if max_v < sum_v:
                max_v = sum_v
    # print는 test case 당 하나
    result = max_v
 
    print(f'#{test_case} {max_v}')
