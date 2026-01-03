# 입력 받기
# a1, a0 순서로 들어옴 (map을 써서 분리)
a1, a0 = map(int, input().split())

# c 입력
c = int(input())

# n0 입력
n0 = int(input())

# 조건 검사
# 1. 시작점(n0)에서 f(n) <= c * n 인가?
# 2. 기울기(a1)가 c보다 작거나 같은가? (a1 <= c)
if (a1 * n0 + a0 <= c * n0) and (a1 <= c):
    print(1)
else:
    print(0)