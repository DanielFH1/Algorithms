import sys

s = sys.stdin.readline().strip()
check_sum = 0 # *을제외한 나머지의 가중치 합합
star_index = -1 # *'s index

for i in range(13):
    if i % 2==0:
        weight = 1 
    else:
        weight = 3 
    
    if s[i] == '*':
        star_index = i
    else:
        check_sum += int(s[i]) * weight 
        
for num in range(10):
    if star_index %2 ==0:
        weight = 1 
    else:
        weight = 3 
    total = check_sum + (weight * num) 
    
    if total % 10 == 0:
        print(num)
        break