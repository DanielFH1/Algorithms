import sys
from collections import deque 

input = sys.stdin.read
data = input().split()

queue = deque()
n = int(data[0])
current_idx = 1

for _ in range(n):
    command = data[current_idx]
    
    if command == "push":
        value = data[current_idx +1]
        queue.append(value)
        current_idx += 2
    else:
        if command == "pop":
            print(queue.popleft() if queue else -1)
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            print(1 if not queue else 0)
        elif command == "front":
            print(queue[0] if queue else -1)
        elif command == "back":
            print(queue[-1] if queue else -1)
        current_idx += 1