"""
SWEA 11649

Original title: 큐_회전_확인용
Topic: Queue rotation
"""

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
 
    # m칸 회전 후 맨 앞에 오는 인덱스는
    # m칸 회전할 때, n칸째 회전할 때마다 원상복귀
    i = m % n
    print(f'#{tc} {arr[i]}')
