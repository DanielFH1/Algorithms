import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    people = [i for i in range(1,n+1)] # 0층의 n호까지의 배열열
    
    for _ in range(k):
        for i in range(1,n):
            people[i] += people[i-1]
    
    print(people[-1])