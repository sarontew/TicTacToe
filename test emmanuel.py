move = 0
grid = {
  1 : [5, 8],
  2: [6, 9]
}
def checkValidMove(grid, move):
  # check the range of move: 1 - 9
  for x in grid[1]:
    if move != x and (move < 9 and move > 0):
      print(grid[1])
      return True
    else:
      print("Error this is not a valid move " + str(move))
      return False
  for x in grid[2]:
    if move != x and (move < 9 and move > 0):
      print(grid[2])
      return True
      
    else:
      print("Error this is not a valid move " + str(move))
      return False
    
    
checkValidMove(grid, 2)