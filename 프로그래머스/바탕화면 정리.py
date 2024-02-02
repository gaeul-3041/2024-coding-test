def solution(wallpaper):
    lux, luy = 50, 50
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lux, luy = min(lux, i), min(luy, j)
                rdx, rdy = max(rdx, i), max(rdy, j)
            
    return [lux, luy, rdx + 1, rdy + 1]