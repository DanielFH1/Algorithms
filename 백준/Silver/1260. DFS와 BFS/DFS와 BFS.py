import sys

def dfs(idx): # idx번 노드부터 탐색하라라
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1,N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
    
def bfs():
    global q, visited
    while q: # q에 요소가 남아있는한 계속
        cur = q.pop(0) # 제일 위에있는거 pop 
        print(cur , end=' ')
        for next in range(1,N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True 
                q.append(next) 
        
    
input = sys.stdin.readline
N,M,V = map(int, input().split())

# graph 정보 입력 (N+1)x(N+1) 2차원 배열
graph = [ [False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1) # visited

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True 
    graph[b][a] = True 
    
dfs(V)
print()
    
# bfs 구현 
visited = [False] * (N+1) # visited False로 다시 초기화
q = [V] # V부터 출발
visited[V] = True


bfs()