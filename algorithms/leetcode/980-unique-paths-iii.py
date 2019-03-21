class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        empty = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 2:
                    ex, ey = i, j
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            if not(x >= 0 and x < m and y >= 0 and y < n and grid[x][y] >= 0):
                return 0
            if x == ex and y == ey:
                if empty == 0:
                    return 1
                else:
                    return 0
            grid[x][y] = -1
            d = dfs(x + 1, y, empty - 1)
            u = dfs(x - 1, y, empty - 1)
            r = dfs(x, y + 1, empty - 1)
            l = dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
            return d + u + r + l
        return dfs(sx, sy, empty)
