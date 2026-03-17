import sys

def insertion_sort(n,k,a):
    count = 0
    
    for i in range(1,n):
        loc = i-1
        new_item = a[i]
        
        while loc >= 0 and new_item < a[loc]:
            a[loc+1] = a[loc]
            count += 1
            
            if count == k:
                return a[loc+1]
            loc -= 1
        if loc+1 != i:
            a[loc+1] = new_item
            count += 1
            
            if count == k:
                return a[loc+1]
    return -1

input_data = sys.stdin.read().split()
if input_data:
    N = int(input_data[0])
    K = int(input_data[1])
    A = list(map(int, input_data[2:]))
    
    print(insertion_sort(N,K,A))