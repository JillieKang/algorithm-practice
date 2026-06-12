"""
SWEA 8702

Original title: 당근 수확
Topic: Consecutive sequence
"""

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    left_sum = 0
    min_diff = float('inf')
    best_cut = 0
    # best cut이 0일때 ~ n-2일 때
    for i in range(n-1):
        left_sum += arr[i]
        right_sum = sum(arr) - left_sum
        diff = abs(left_sum - right_sum)
        if min_diff > diff:
            min_diff = diff
            best_cut = i
 
    print(f'#{tc} {best_cut + 1} {min_diff}')
