"""
SWEA 12395

Original title: 문자열_글자수
Topic: Character frequency
"""

T = int(input())
for test_case in range(1, T+1):
    # str1만 내부의 중복 제거
    str1 = list(set(input()))
    str2 = input()
 
    # str1 속 글자가 str2 속에 있는지 검사
    # str1의 길이만큼 빈 리스트를 만들어서
    # str1 속 해당 글자가 str2 속에 있을 때마다 1씩 count(+=)한 다음
    # 가장 큰 값의 인덱스를 이용
    count = [0]*len(str1)
    # str1 중 하나를 골라
    for i in range(len(str1)):
        # i를 str2 속 j들과 일일이 대조하자
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count[i] += 1
              
    print(f'#{test_case} {max(count)}')
