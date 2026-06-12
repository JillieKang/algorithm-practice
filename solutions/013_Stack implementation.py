"""
SWEA 12396

Original title: 스택1_괄호검사
Topic: Stack implementation
"""
 
def my_push(item, size):
    # global top을 사용하고
    global top
    # 먼저 overflow 검사
    if top == size - 1:
        # 만약 top이라는 idx가 이미 arr의 맨 끝이라면
        return
    # 정상 상황이라면
    else:
        # top 하나 늘리고
        top += 1
        # 늘린 top 위치에 item을 넣어
        stack[top] = item
 
 
def my_pop():
    global top
    # 먼저 underflow 검사
    if top == -1:
        return
    else:
        top -= 1
        return stack[top+1]
 
T = int(input())
for test_case in range(1, T+1):
    # top의 초기값 -1
    top = -1
    arr = input()
 
    # 빈 stack을 생성한 다음
    stack = [0]*len(arr)
    # 일단 ans는 잘 됐다고 상정하고, 틀린 결과 만날 때마다 '틀렸음' 업데이트
    ans = 1
 
    # arr 안의 하나하나 요소들을 순회
    for i in arr:
        # 여는 괄호를 만난다면
        if i in '({':
            my_push(i, len(arr))
        elif i in ')}':
            popped_top = my_pop()
            if i == ')' and popped_top != '(':
                ans = 0
                break
            elif i == '}' and popped_top != '{':
                ans = 0
                break
 
    # 한 test_case에 대해 연산 끝났을 때
    # stack이 안비었으면 => 닫는 괄호가 존재하지 않음
    if top != -1:
        ans = 0
 
    print(f'#{test_case} {ans}')
