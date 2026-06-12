"""
SWEA 26045

Original title: 부분 수열 판별
Topic: Subsequence check
"""

T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    def seek_num(A, B):
        idx_b = 0
        for i in A:
            if idx_b == len(B):
                break
 
            if i == B[idx_b]:
                idx_b += 1
 
        if idx_b == len(B):
            return True
        else:
            return False
 
    result = seek_num(A, B)
 
    yes_no =''
 
    if result == True:
        yes_no = 'YES'
    else:
        yes_no = 'NO'
 
    print(f'#{test_case} {yes_no}')
