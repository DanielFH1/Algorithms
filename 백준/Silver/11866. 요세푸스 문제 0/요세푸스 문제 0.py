import sys
from collections import deque

input = sys.stdin.read().split()
N = int(input[0])
K = int(input[1])

queue = deque(range(1,N+1))
result = []

while queue:
    for _ in range(K-1):
        person = queue.popleft()
        queue.append(person)
    removed_person = queue.popleft()
    result.append(str(removed_person))
    
print("<" + ", ".join(result) + ">")
    
    