import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

queue = deque(range(1,N+1)) # (1,N] 까지의 queue생성
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])