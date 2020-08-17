class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) // 2
            if self.is_possible(nums, mid, m):
                r = mid
            else:
                l = mid + 1
        return l
    
    def is_possible(self, nums, mid, m):
        tot = 0
        cnt = 1
        for n in nums:
            tot += n
            if tot > mid:
                cnt += 1
                tot = n
            if cnt > m:
                return False
        return True
