class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:       
        pre_sum = [0]
        for v in stoneValue:
            pre_sum.append(pre_sum[-1] + v)
        
        @lru_cache(None)
        def dfs(i, j):
            res = 0
            for k in range(i, j):
                if pre_sum[k] - pre_sum[i - 1] <= pre_sum[j] - pre_sum[k]:
                    res = max(res, pre_sum[k] - pre_sum[i - 1] + dfs(i, k))
                if pre_sum[k] - pre_sum[i - 1] >= pre_sum[j] - pre_sum[k]:
                    res = max(res, pre_sum[j] - pre_sum[k] + dfs(k + 1, j))
            return res
        return dfs(1, len(pre_sum) - 1)
