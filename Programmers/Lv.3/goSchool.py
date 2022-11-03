# 프로그래머스 등굣길

def solution(m, n, puddles):
    answer = 0
    loc = []
    for i in range(n+1):
        loc_ = []
        for j in range(m+1):
            loc_.append(0)        
        loc.append(loc_)
    
    for p in puddles:
        x, y = p[1], p[0]
        loc[x][y] = -1
        
    loc[1][1] = 1    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if loc[i][j] == -1:
                loc[i][j] = 0
                continue
            loc[i][j] = (loc[i-1][j] + loc[i][j-1]) % 1000000007
            
    
    return loc[n][m]