import sys

a,b = map(int, sys.stdin.readline().split())

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

r_gcd = gcd(a,b)
r_lcm = (a*b) // r_gcd

print(r_gcd)
print(r_lcm)