"""
SWEA 12387

Original title: 배열1_구간합_확인용
Topic: Maximum range sum
"""

T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    max_sum = -float('inf')
    min_sum = float('inf')

    # 첫 j는 i번부터 시작
    # 구간의 마지막 j는 i i+1 i+2 => i+M-1번
    # range(i+M)
    for i in range(N-M+1):
        current_sum = 0

        for j in range(i, i+M):
            current_sum += ai[j]
 
        # 하나의 구간에 대해 current_sum을 완성한 다음
        # 비교해서 max_sum, min_sum 업데이트 여부 결정
        if max_sum < current_sum:
            max_sum = current_sum
        if min_sum > current_sum:
            min_sum = current_sum
 
    # print는 max_sum과 min_sum을 완성한 다음
    # case_test 당 하나씩
    print(f'#{test_case} {max_sum-min_sum}')
