"""
SWEA 11613

Original title: 스택2_Forth
Topic: Stack evaluation
"""

# 이미 후위표기법으로 변환 완료 상태임
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1}
 
def stack_cal(arr):
    for token in arr:
        # .을 만나면 스택에서 숫자를 꺼내어 출력
        if token == '.':
            # pop 전에는 항상 스택 길이 검사
            # 만약 1개보다 더 많은 요소가 남아있으면 None 반환
            if len(s) != 1:
                return None
            # 정상이면 pop()
            return s.pop()
 
        # 연산자가 아니면(숫자면) 숫자로 변환
        elif token not in isp.keys():
            s.append(int(token))
 
        # 연산자를 만나면 스택의 숫자 두 개 꺼내어 연산,
        # 그 결과는 스택에 삽입
        elif token in isp.keys():
            # 스택에 숫자가 2개 이상 존재하지 않을 경우
            if len(s) < 2:
                return None
            b, a = s.pop(), s.pop()
            if token == '*':
                s.append(a * b)
            elif token == '/':
                s.append(a // b)
            elif token == '+':
                s.append(a + b)
            elif token == '-':
                s.append(a - b)
 
t = int(input())
for tc in range(1, t+1):
    arr = list(input().split())
    s = []
    result = stack_cal(arr)
    if result is None:
        result = 'error'
 
    print(f'#{tc} {result}')
