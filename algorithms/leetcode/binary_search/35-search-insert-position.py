import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)
        

    def searchInsert2(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
#            if nums[m] == target:
#                return m
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l
