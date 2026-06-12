"""
SWEA 12391

Original title: 배열2_이진탐색_확인용
Topic: Binary search
"""

# 일단 p에서 pa를 탐색
def bi_search(p, key):
    # 1부터 p까지의 숫자에서 누가 더 큰 count를 기록하는지 비교
    l = 1
    r = p
 
    cnt = 0
 
    # l == r일 때까지는 작동
    # l > r 되면 중단
    while l < r:
        c = (l+r)//2
        cnt += 1
 
        if c == key:
            return cnt
        elif c > key:
            r = c 
        else:
            l = c 
 
T = int(input())
for test_case in range(1, T+1):
    p, pa, pb = map(int, input().split())
 
    # 위에서 만들어둔 함수를 pa와 pb에 대해 실행한 다음
    # 그 카운트를 서로 비교한다
    a_result = bi_search(p, pa)
    b_result = bi_search(p, pb)
 
    # a가 b보다 오래걸렸으면
    if a_result > b_result:
        result = 'B'
    # b가 a보다 오래걸렸으면
    elif a_result < b_result:
        result = 'A'
    elif a_result == b_result:
        result = 0
 
    print(f'#{test_case} {result}')
