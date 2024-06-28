grid = {
        1: [4, 8],
        2: [3, 2]
    }

def updateGridWithMove(grid, move, playernumber):

    if playernumber == 1:
       grid[1].append(move)

    if playernumber == 2:
       grid[2].append(move)
   
    print(grid)
        
def main():
    updateGridWithMove(grid, 6, 1)

if __name__ == "__main__":
  main()