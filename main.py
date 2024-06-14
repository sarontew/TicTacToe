
def checkwin(grid):
    
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != '':
            print("Player", row[0], "wins!")  
            return row[0]  
    
    
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '':
            print("Player", grid[0][col], "wins!")  
            return grid[0][col]  
    
    
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '':
        print("Player", grid[0][0], "wins!")  
        return grid[0][0]  
    
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '':
        print("Player", grid[0][2], "wins!") 
        return grid[0][2]  
    
    
    print("No winner yet!")  
    return None  


grid = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]

checkwin(grid)
