import sys

n = int(sys.stdin.readline())

def solve_normal(n):
    result = 1 
    for i in range(1,n+1):
        result *= i 
    return result 
    
print(solve_normal(n))