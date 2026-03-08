n= int(input())
A = [int(input()) for _ in range(n)]

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if A[min_index] > A[j]:
            min_index = j
    if min_index != i:
        A[min_index], A[i] = A[i] , A[min_index]
        
for num in A:
    print(num)