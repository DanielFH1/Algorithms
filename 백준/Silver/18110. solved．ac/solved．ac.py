import sys

def custom_round(num):
    return int(num + 0.5)

def solve():
    input = sys.stdin.readline
    n = int(input())
    
    if n==0:
        print(0)
        return
    votes = [int(input()) for _ in range(n)]
    votes.sort()
    
    trim_count = custom_round(n*0.15)
    if trim_count >0:
        valid_votes = votes[trim_count: -trim_count]
    else:
        valid_votes = votes
    average = sum(valid_votes) / len(valid_votes)
    print(custom_round(average))
    
if __name__ == '__main__':
    solve()