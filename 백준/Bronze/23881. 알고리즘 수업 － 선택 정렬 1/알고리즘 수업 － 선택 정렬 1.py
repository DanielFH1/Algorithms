import sys

def selection_sort():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = list(list(map(int,input().split())))
    
    count = 0
    
    for last in range(N-1, 0, -1):
        max_idx = 0
        for i in range(0,last+1):
            if A[i] > A[max_idx]:
                max_idx = i
                
        if max_idx != last:
            A[last], A[max_idx] = A[max_idx], A[last]
            count += 1
            if count == K:
                print(A[max_idx], A[last])
                return
            
    print(-1)
    
selection_sort()