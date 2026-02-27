import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    s = sys.stdin.readline().rstrip()
    is_vps = True
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")