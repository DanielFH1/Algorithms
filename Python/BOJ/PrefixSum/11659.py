# 합배열 공식 : S[i] = S[i-1] + A[i]
# 구간합 공식(i~j) : S[j] - S[i-1]
# 예시 : 5 4 3 2 1 
# (1,3) : S[3] - S[0] = (5+4+3) - 0 = 12
# (2,4) : S[4] - S[1] = (5+4+3+2) - (5) = 9

# Pseudo 
# N = 숫자개수, quizN = 질의 개수
# numbers에 숫자 저장
# prefix_sum 에 합배열
# temp 

# for loop in numbers : prefix_sum 에 temp값 저장 -> 합배열 완성
# for 질의 개수만큼 : 질의 범위 받기(i,j) -> 구간합 출력 (prefix_sum[e] - prefix_sum[s-1])
import sys 

N , quizNo = map(int, sys.stdin.readline().split())
numbers = list(map(int, input().split())) # 5 4 3 2 1
prefix_sum = [0] # padding
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    a,b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b] - prefix_sum[a-1])