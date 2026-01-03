import sys

N = int(input())

data = []

for _ in range(N):
    w,h = map(int, sys.stdin.readline().split())
    data.append((w,h))

for i in range(N):
    count = 0
    for j in range(N):
        if (data[j][0]>data[i][0]) and (data[j][1]>data[i][1]):
            count += 1
    print(count+1, end=' ')