import sys
n,m = map(int, sys.stdin.readline().split()) # n : 행렬 크기, m : 질의 수

A = [ [0] * (n+1) ]# A : 원본 리스트, S : 합 리스트
D = [ [0] * (n+1) for _ in range(n+1)]

for i in range(n):# 원본 저장 (for loop)
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):# 합 배열 만들기
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for i in range(m): # 공식으로 질의에 대한 정답 계산
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    ans = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(ans)