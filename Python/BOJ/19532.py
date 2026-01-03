# 이중 반복 : O(n^2)
import sys

# input().split()은 \n 이런거 제외하고 가져와서 오래걸리는데, 이건 버퍼 통째로 다 긁어와서 빠름
a,b,c,d,e,f = map(int, sys.stdin.readline().split())

for x in range(-999,1000):
    for y in range(-999, 1000):
        if( (a*x) + (b*y) == c) and (d*x) + (e*y)==f:
            print(x,y)
            break

'''
# O(1)
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (c*e - b*f) // (a*e - b*d)
y = (a*f - c*d) // (a*e - b*d)

print(x, y)
'''