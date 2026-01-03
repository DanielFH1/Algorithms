# 규칙이 복잡하면 brute force
# 정답 숫자가 대충 얼마나 커질지" 감을 잡았을 때, 그 숫자가 1억보다 한참 작다면 **"1부터 다 세어보기(브루트포스)"**가 가장 좋은 해결책입니다.
import sys

N = int(input())

name = 666
count = 0

while True:
    if '666' in str(name):
        count += 1
    if count == N:
        print(name)
        break 
    name += 1