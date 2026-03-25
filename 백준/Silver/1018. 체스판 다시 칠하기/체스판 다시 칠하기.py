import sys

def solve():
    input = sys.stdin.readline
    N,M = map(int,input().split())
    board = [input().strip() for _ in range(N)]
    
    min_paint = float('inf')
    
    for i in range(N-7):
        for j in range(M-7):
            paint_w, paint_b = 0,0
            
            for x in range(8):
                for y in range(8):
                    current_color = board[i+x][j+y]
                    
                    if (x+y)%2 == 0:
                        if current_color != 'W': paint_w += 1
                        if current_color != 'B': paint_b += 1
                    else:
                        if current_color != 'W': paint_b += 1
                        if current_color != 'B': paint_w += 1
            min_paint = min(min_paint, paint_w, paint_b)
    print(min_paint)
if __name__ == '__main__':
    solve()