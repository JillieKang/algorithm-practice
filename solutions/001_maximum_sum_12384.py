T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
 
    max_sum = 0
    sum_now = 0
    for i in range(N-1):
        sum_now = ai[i] + ai[i+1]
        if max_sum < sum_now:
            max_sum = sum_now
 
    print(f'#{test_case} {max_sum}')
