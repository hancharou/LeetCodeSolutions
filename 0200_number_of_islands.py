from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x-1 >= 0 and grid[x-1][y] == '1':
                grid[x-1][y] = '0'
                dfs(x-1, y)
            if x + 1 < vertical and grid[x+1][y] == '1':
                grid[x+1][y] = '0'
                dfs(x+1, y)
            if y - 1 >= 0 and grid[x][y-1] == '1':
                grid[x][y-1] = '0'
                dfs(x, y-1)
            if y + 1 < horizontal and grid[x][y+1] == '1':
                grid[x][y+1] = '0'
                dfs(x, y+1)

        vertical = len(grid)
        horizontal = len(grid[0])
        i, result = 0, 0
        while i < vertical:
            j = 0
            while j < horizontal:
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    result += 1
                    dfs(i, j)
                j += 1
            i += 1

        return result


if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert s.numIslands(grid) == 3

    grid2 = [["1","1","1"],
             ["0","1","0"],
             ["0","1","0"]]
    assert s.numIslands(grid2) == 1


