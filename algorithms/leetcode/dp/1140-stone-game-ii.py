    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.visited = {}
        return self.dfs(piles, len(piles), 0, 2)

    def dfs(self, piles, n, i, j):
        if i >= n:
            return 0
        if (i, j) in self.visited:
            return self.visited[(i, j)]

        j = min(j, n - i)
        stones = sum(piles[i:])
        if n - i == j:
            self.visited[(i, j)] = stones
            return stones

        min_dp = float('inf')
        for k in range(1, j + 1):
            min_dp = min(min_dp, self.dfs(piles, n, i + k, max(j, 2 * k)))
        self.visited[(i, j)] = stones - min_dp
        return stones - min_dp 

    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(maxsize=None)
        def minimax(st, m, player):
            if st >= len(piles): return 0
            if player:
                return max([sum(piles[st:st+x]) + minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
            else:
                return min([minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
        return minimax(0, 1, 1)   
