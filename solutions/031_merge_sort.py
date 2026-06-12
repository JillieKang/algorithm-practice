"""
SWEA 11891

Original title: 분할정복_병합정렬
Topic: Merge sort
"""

# 병합 정렬

# 배열을 계속 반으로 나누며 재귀적 정렬
# 배열의 왼쪽 반, 오른쪽 반을 함수에 넣어서 호출하는 식으로 계속 나눔
# 기저조건: 그 길이가 <= 1 (이미 정렬 완료 상태)

# 더 이상 나눌 수 없다면 합치기 시작
# 왼쪽의 i와 오른쪽의 j를 0부터 증가시켜가며 서로 비교
# 더 작은 값부터 결과 리스트에 삽입

# 한쪽 리스트의 요소가 모두 삽입 완료 되었다면
# 나머지 한쪽 리스트의 남은 값들은 그대로 결과 리스트에 삽입
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    right_cnt = 0
 
    def merge_sort(arr):
        if len(arr) <= 1:   # 기저조건
            return arr
 
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])    # left에 mid 포함 안 됨
        right = merge_sort(arr[mid:])
 
        # left의 마지막 원소는 n // 2 - 1 번
        # right의 마지막 원소는 n - 1번
 
        sorted_arr = []
        i = len(left) - 1
        j = len(right) - 1
 
        global right_cnt
        # left와 right를 합치자.
        if left[i] > right[j]:
           right_cnt += 1
        while i >= 0 and j >= 0:    # i >= 0 일때까지 실행
            if right[j] > left[i]:
                sorted_arr.append(right[j])
                j -= 1
            else:
                sorted_arr.append(left[i])
                i -= 1
 
        # while문이 끝났는데도 i == len(left) 아니라면
        while i >= 0:
            sorted_arr.append(left[i])
            i -= 1
 
        while j >= 0:
            sorted_arr.append(right[j])
            j -= 1
 
        sorted_arr.reverse()
        return sorted_arr
 
    print(f'#{tc} {merge_sort(arr)[n//2]} {right_cnt}')
