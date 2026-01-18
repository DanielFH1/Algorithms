import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(row,col):
    if row<0 or row>= h or col <0 or col>= w or graph[row][col] == 0:
        return
    graph[row][col] = 0
    
    dr = [1,-1,0,0,1,1,-1,-1]
    dc = [0,0,-1,1,1,-1,1,-1]
    
    for i in range(8):
        nr = row + dr[i]
        nc = col + dc[i]
        dfs(nr,nc)

while True:
    w,h = map(int, input().split())
    
    if (w==0 and h==0):
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
        
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                dfs(i,j)
    print(count)