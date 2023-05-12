'''

Given a grid and shift operation,
return a new grid

Steps: 
  determine the size of the grid, assign numerical 
  value to each location.
  shift each element by the shift operation,
  if the shift brings the element to a point beyond, loop to start

'''
class Solution():
  def prepGrid(self, grid):
    rows = 0
    columns = 0
    gridList = []
    for row in grid:
      rows += 1
      for value in row:
        gridList.append(value)
    for column in grid[0]:
      columns += 1
    return (gridList, (rows, columns))
    
  def shiftGrid(self, grid, shift):
    # get data for operating on grid
    gridData = self.prepGrid(grid)

    # shift deconstructed grid
    gridList = gridData[0]
    for i in range(shift):
      gridList.insert(0, gridList[-1])
      gridList.pop()

    # reconstruct grid
    dimensions = gridData[1]
    new_grid = []
    row_pointer = 0
    value_pointer = 0

    for rows in range(dimensions[0]):
      new_grid.append([])
      for columns in range(dimensions[1]):
        new_grid[row_pointer].append(gridList[value_pointer])
        value_pointer += 1
      row_pointer += 1
    return new_grid

solution = Solution()
print(solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
