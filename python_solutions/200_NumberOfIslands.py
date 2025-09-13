class Solution:
    def numberOfIslands(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        island_ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island_ct += 1
        return island_ct
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] == '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
def test_solution():
    solution = Solution()
    sample_island =  [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    print(f"Test1: {solution.numberOfIslands(sample_island)}")
if __name__ == "__main__":
    test_solution()