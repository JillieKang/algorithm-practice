"""
SWEA 4837

Original title: 부분집합의 합
Topic: Subset generation
"""

# 모든 부분집합을 생성
# 원소의 개수를 세서 n과 같으면 >> 합을 계산 
# 합이 k와 같으면 >> 전역변수에 += 1
 
t = int(input())
m = 12
 
# 집합 a 생성
a = []
for i in range(1, m+1):
    a.append(i)
 
# 부분집합 전체 생성
sub_list = []
for i in range(1 << m):
    subset = []
    for j in range(m):
        if i & (1 << j):
            subset.append(a[j])
    sub_list.append(subset)
 
# test case마다 n과 k 계산
 
for tc in range(1, t+1):
    n, k = map(int, input().split())
 
    cnt = 0
    for i in sub_list:
        if len(i) == n:
            if sum(i) == k:
                cnt += 1
 
    print(f'#{tc} {cnt}')
