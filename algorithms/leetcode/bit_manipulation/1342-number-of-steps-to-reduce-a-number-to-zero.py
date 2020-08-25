class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            res += 1
        return res

    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while num:
            res += (num & 1) + 1
            num >>= 1
        return res - 1
