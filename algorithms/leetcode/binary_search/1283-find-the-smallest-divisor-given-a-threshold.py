class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if sum((num - 1) // m + 1 for num in nums) <= threshold:
                r = m
            else:
                l = m + 1
        return l
