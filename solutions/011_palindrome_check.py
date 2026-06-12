"""
SWEA 12394

Original title: 문자열_회문_확인용
Topic: Palindrome check
"""

T = int(input())
 
# n은 원본의 가로세로길이, m은 찾고자 하는 회문의 길이
 
# 하나의 row에 대해서 길이가 m인 회문을 찾는 function
def seek(row, m):
    # 시작 인덱스는 항상 리스트의 길이 // 2
    for i in range(m//2):
        # (해당 열의 시작 인덱스)번 요소가 비교대상과 다르다면
        # 구간의 맨끝번 - i 번이 비교대상임
          # i=0일 때 n-1번
          # i=1일 때 n-2번이기에
        if row[i] != row[m-1-i]:
            return None
    # 만약 if가 한 번도 참이 되지 않은 채 for문이 끝났다면
    # 회문이라면 해당 row를 반환
    return row
 
 
for tc in range(T):
    n, m = map(int, input().split())
    # list comprehension의 input은 iterable하기만 하면 됨
    str1 = [input() for _ in range(n)]
 
    # 가로 방향 탐색
    for i in str1:
        # 시작 인덱스는 0번부터 n-m번까지 돌아야 함
        for start in range(n-m+1):
            # str1 속 하나의 row 속에서
            # 길이가 m인 구간을 생성
            sub = i[start:start+m]
            # str1 속 하나의 row 속에서 가능한 모든 길이 m 구간에 대해 result를 생성
            result = seek(sub, m)
            # 만약 이번 구간에서 찾았으면 break
            if result is not None:
                break   # for start
        # 만약 이번 row에서 찾았으면 break
        if result is not None:
            break
 
    # 세로 방향 탐색
    # 만약 가로 탐색을 실패했다면
    if result is None:
        for c in range(n):
            # c를 바꿀 때마다 새로운 col을 생성
            col = ""
            # c는 하나로 선택해두고, r을 변경
            # r은 0부터 n-1까지
            for r in range(n):
                col += str1[r][c]
            # 하나의 col이 완성되었으면, 그 안에서 길이 m인 구간 반복 생성
            for start in range(n-m+1):
                sub = col[start:start+m]
                result = seek(sub, m)
                # 만약 이번 sub속에서 찾았으면 break
                # 못 찾았으면 다음 sub 생성한 다음
                if result is not None:
                    break
            # 만약 이번 col 속에서 찾았으면 break
            # 못 찾았으면 다음 col 생성한 다음
            if result is not None:
                break

    print(f'#{tc+1} {result}')
