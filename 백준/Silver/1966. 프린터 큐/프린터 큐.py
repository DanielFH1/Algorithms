import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        N,M = map(int,input().split())
        priorities = list(map(int, input().split()))
        
        queue = deque([val,idx] for idx,val in enumerate(priorities))
        
        print_order = 0
        
        while queue:
            current = queue.popleft()
            
            if any(current[0] < q[0] for q in queue):
                queue.append(current)
            else:
                print_order+= 1
                if current[1] == M:
                    print(print_order)
                    break
        
        
    
if __name__ == '__main__':
    solve()