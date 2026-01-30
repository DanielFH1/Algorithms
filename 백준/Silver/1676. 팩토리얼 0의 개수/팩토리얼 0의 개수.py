import sys
input = sys.stdin.readline

N = int(input())

count = 0
i = 5

while i<= N:
    count += N//i
    i = i* 5
    
print(count)