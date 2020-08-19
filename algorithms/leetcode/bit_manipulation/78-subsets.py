class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            res += [ r + [n] for r in res]
        return res

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        for i in range(1<<n):
            tmp = []
            for j in range(n):
                if i & 1 << j:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    # DFS
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res) 
