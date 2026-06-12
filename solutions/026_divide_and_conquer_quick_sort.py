"""
SWEA 11892

Original title: 분할정복_퀵정렬
Topic: Quick sort
"""

# 퀵 정렬
# pivot을 기준으로 작거나 같은 값은 왼쪽으로, 큰 값은 오른쪽으로 이동
# 이동 완료시, i와 j가 교차한 지점으로 pivot의 위치를 이동
# 그 다음 왼쪽그룹 / 오른쪽 그룹에 대해서 재귀호출 실행
 
def quick(lo, hi):
    i, j = lo, hi
 
    # 재귀호출 끝내는 조건: lo == hi면 숫자 하나만 남음 = 이미 정렬 완료
    # lo > hi는 논리적으로 잘못된 인덱스
    if lo >= hi:
        return
 
    # i와 j가 교차하기 전까지
    while i <= j:
        # i에 대해 인덱스 검사: i는 오른쪽으로 계속 증가
        # pivot보다 작거나 같은 값인 경우 무시
        while i <= hi and arr[i] <= arr[lo]:
            i += 1
        # j는 pivot보다 작거나 같은 값보면 멈춤
        # pivot보다 큰 값인 경우 무시
        while j >= lo and arr[j] > arr[lo]:
            j -= 1
 
        # i와 j가 교차하기 전, i와 j를 찾았으면 그 둘을 교환
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
 
    # i와 j가 교차했다면 그 자리로 pivot을 이동
    # j는 작거나 같은 그룹의 오른쪽끝
    # i는 큰 그룹의 왼쪽끝이므로
    # arr[j]와 pivot을 서로 바꿔야 함
 
    arr[lo], arr[j] = arr[j], arr[lo]
    quick(lo, j - 1)
    quick(j + 1, hi)
 
 
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    quick(0, len(arr) - 1)
    ans = arr[n//2]
  
    print(f'#{tc} {ans}')
