T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    max_fall = 0
    for i in range(N):  # 각 test case마다, N개의 건물들(0번 건물 ~ N-1번 건물)에 대해 모두 작업 수행
 
        now_fall = 0
        for j in range(i+1, N):  # i번째 건물의 바로 오른쪽 건물부터 끝번 건물까지 비교해야 함
            if arr[i] > arr[j]:  # i번째 건물이 j번째 건물보다 크다면
                now_fall += 1    # i번째 건물과 j번째 건물을 비교할 때마다 += 업데이트 여부 결정
 
        if max_fall < now_fall:     # i번째 건물에 대해서 N-1번째 건물까지 다 돌아서 now_fall을 업데이트 한 다음
            max_fall = now_fall     # 만약 이 i번째 건물의 최종 now_fall이 max_fall보다 크다면 max_fall을 업데이트
                                    # max_fall은 i번째 건물의 now_fall이 완성 될 때마다 비교 후 업데이트 여부 결정
 
    print(f'#{test_case} {max_fall}')   # print() test case for문에 걸리게
