"""
SWEA 2806

Original title: N-Queen
Topic: N-Queens backtracking
"""

# nqueen
# 행마다 어떤 열에 퀸을 놓을 것인지 결정해야 함
# 방문표시된 열, 대각선1, 대각선2라면 그곳에는 놓을 수 없음 >> continue
 
t = int(input())
for tc in range(1, t+1):
 
    n = int(input())
    # col에 방문표시
    column = [0] * n    
    # 우하향 대각선 방문표시
    # 같은 대각선끼리는 row+col 값이 같음
    # 가능한 값은 0~2n-2임 >> 배열 크기 2n-1
    line1 = [0] * (n+n-1)   
    line2 = [0] * (n+n-1)
 
    ans = 0
    def nqueen(row):
        # 재귀 끝내는 조건: 모든 row에 대해 퀸 다 놓았을 때
        if row == n:    
            global ans; ans += 1
            return
          
       # 매 행마다, 0번부터 n-1번까지 열을 순회하며 어느 열에 놓을 건지 결정
        for col in range(n):    
            a = row + col
            b = row - col + n - 1
          
            # col line1 line2 뭐라도 하나 방문처리 되어 있다면 >> continue
            if column[col] or line1[a] or line2[b] == 1:    
                continue
              
            else:
                column[col] = line1[a] = line2[b] = 1
                nqueen(row + 1)
                column[col] = line1[a] = line2[b] = 0
 
    nqueen(0)
  
    print(f'#{tc} {ans}')
