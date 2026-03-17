import sys 
n = int(sys.stdin.readline())
arr =  []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
    
for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = key
    
for num in arr:
    print(num)
