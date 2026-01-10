import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())

stack = [] 

for _ in range(n):
    command = sys.stdin.readline().split()
    cmd_type = command[0]
    
    if cmd_type == 'push':
        stack.append(int(command[1]))
    elif cmd_type =='pop':
        print(stack.pop()) if stack else print(-1)
    elif cmd_type == 'size':
        print(len(stack))
    elif cmd_type == 'empty':
        print(1) if not stack else print(0)
    elif cmd_type == 'top':
        print(-1) if not stack else print(stack[-1])
        