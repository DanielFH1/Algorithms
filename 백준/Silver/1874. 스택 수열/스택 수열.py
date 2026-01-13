import sys 

input = sys.stdin.readline

n = int(input()) # 숫자의 개수 n 
stack = [] 
result = [] # +,- 담을거
count = 1 
is_possible = True 

for _ in range(n):
    target = int(input())
    
    # 1. 목표숫자(target)가 될때까지 숫자를 스택에 넣는다.
    while count <= target:
        stack.append(count)
        result.append('+')
        count += 1 
        
    # 2. 스택의 맨위 숫자가 목표 숫자와 같은지 확인함 
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        is_possible = False
        break 
if is_possible == False:
    print("NO")
else:
    for op in result:
        print(op)