import sys
from collections import Counter

input = sys.stdin.read
data = input().split()

# 나는 n개, target은 m개
n = int(data[0])
cards = data[1:n+1]
m = int(data[n+1])
targets = data[n+2:]

count_table = Counter(cards)
result = []

for x in targets:
    result.append(str(count_table[x]))
    
print(" ".join(result))
