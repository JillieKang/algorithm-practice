"""
SWEA 1240

Original title: 단순 2진 암호코드
Topic: Binary pattern decoding
"""

codes = {
    (0,0,0,1,1,0,1): 0,
    (0,0,1,1,0,0,1): 1,
    (0,0,1,0,0,1,1): 2,
    (0,1,1,1,1,0,1): 3,
    (0,1,0,0,0,1,1): 4,
    (0,1,1,0,0,0,1): 5,
    (0,1,0,1,1,1,1): 6,
    (0,1,1,1,0,1,1): 7,
    (0,1,1,0,1,1,1): 8,
    (0,0,0,1,0,1,1): 9,
}
 
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
 
    found = False
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] != 0:
                barcode = arr[i][j-55:j+1]
                nums = []
                for k in range(8):
                    bits = tuple(barcode[k*7:(k+1)*7])
                    nums.append(codes[bits])
                found = True
                break
        if found:
            break
 
    # checksum validation 실행
    # 홀수 자리(index 0,2,4,6) * 3 + 짝수 자리(index 1,3,5,7)
    check = 0
    for i in range(8):
        if i % 2 == 0:
            check += nums[i] * 3
        else:
            check += nums[i]
 
    ans = 0
    if check % 10 == 0:
        ans = sum(nums)
 
    print(f'#{tc} {ans}')
