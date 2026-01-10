import sys

L = int(sys.stdin.readline()) # 문자열 길이 L 
string = sys.stdin.readline().strip() # input 으로 들어오는 문자열

r=31
M = 1234567891
total_sum = 0

for i in range(L):
    num = ord(string[i]) - ord('a') + 1 
    total_sum += num * (r ** i)
    
total_sum = total_sum % M 

print(total_sum)



# 해쉬 구현