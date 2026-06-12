"""
SWEA 12388

Original title: 배열2_색칠하기_확인용
Topic: Grid traversal and coloring
"""

T = int(input())
 
for test_case in range(1, T+1):
    blank = [[0]*10 for i in range(10)]
    N = int(input())
 
    # N줄의 인풋이 들어오면 N줄을 다 받아야 함
    for i in range(N):
        r1, c1, r2, c2, colour = map(int, input().split())
 
        # 인풋을 받을 때마다 색칠을 해야 함
        # r1번부터 r2번까지의 모든 행을 고르자
        for r in range(r1, r2+1):
            # 그 안에서 c1번부터 c2번 열까지의 모든 요소들을 순회하자
            for c in range(c1, c2+1):
                # 순회의 대상이 되는 작은 박스 속 모든 요소에 대해
                # colour 값을
                # i가 0번부터 N-1번이 되도록 계속 반복해서 colour을 더해야 함
                blank[r][c] += colour
 
    # i가 0번부터 N-1번 되도록 다 순회해서 모든 colour을 다 칠한 다음
    # test case 하나 전체에서 counts를 세자
    counts = 0
    # 0번부터 9번까지의 행을 선택해서
    for r in range(10):
        # 그 안에 있는 0번열부터 9번열까지의 요소를 순회하며
        for c in range(10):
            if blank[r][c] >= 3:
                counts += 1

    print(f'#{test_case} {counts}')
