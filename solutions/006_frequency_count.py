"""
SWEA 12386

Original title: 배열1_숫자카드_확인용
Topic: Frequency count
"""

T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))
    temp = [0] * N
    counts = [0] * (9+1)    # 제약사항: ai 속 요소들 중 최대값은 9
 
    # 1단계: 개수 세기
    # ai라는 자료 안에서 0을 만나면 counts[0]에 1을 더해주자
    for val in ai:
        counts[val] += 1
        
 
    simple_counts = counts[:]
 
    # 2단계: 누적합 구하기
    # counts[1]에는 counts[0] + counts[1]을 저장해주자
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i-1]
 
    # 3단계: counts[2]의 누적합이 5면, temp의 4번 인덱스에 2를 저장
    
    # 어디서부터 어디까지?
      # counts는 0 1 2 3 4 5 6 7 8 9, 9번 인덱스까지 10개
      # i는 9번 인덱스부터 0번 인덱스까지 돌아야 함
      # range(len(counts)-1, -1, -1)
        # 9 = len(counts)-1
        # range를 0까지 만들어야 하니까 stop은 0이 아니라 -1로
        # step은 뒤에서부터 거꾸로 방향이니까 -1
 
    # ai[3] = 2고 그 누적개수합은 5라고 해보자
    # temp[누적합-1]이 필요
      # counts[ai[3]] = counts[2] => 2의 누적합
      # counts[j] -= 1로 미리 1씩 마이너스
      # temp[누적합-1] = temp[counts[ai[j]]]
      # 여기에 2를 저장 2 = ai[j]
      # ai[3] = 2
      # counts[ai[3]] = counts[2] = 2의 누적합 = 5
      # 5-1을 temp의 인덱스로 사용(다섯번째 자리 = 4번 인덱스 자리)
      # 그래서 미리 counts[j] -= 1 수행한 다음
      # temp[counts[ai[3]]] = ai[3]
      # temp[counts[data[j]]] = data[j]
  
    for j in range(len(ai)-1, -1, -1):
        counts[ai[j]] -= 1
        temp[counts[ai[j]]] = ai[j]
 
 
    # 0부터 9까지 숫자들의 개수가 들어 있는 simple_counts
    # 그 중에서 max 탐색
    max_count = 0
    for m in simple_counts:
        if m > max_count:
            max_count = m
 
    max_val = 0
    for i in range(len(simple_counts)):
        if simple_counts[i] == max_count:
            max_val = i
 
    print(f'#{test_case} {max_val} {max_count}')
