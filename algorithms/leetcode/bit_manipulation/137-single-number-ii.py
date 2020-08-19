class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) // 2

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0
        for n in nums:
            ones = (ones^n) & ~twos
            twos = (twos^n) & ~ones
        return ones
