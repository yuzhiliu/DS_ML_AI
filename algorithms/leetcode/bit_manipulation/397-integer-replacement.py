class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        level = set()
        level.add(n)
        res = 0
        while level:
            next_level = set()
            if 1 in level:
                return res
            for num in level:
                if num % 2 == 0:
                    next_level.add( num / 2)
                else:
                    next_level.add( num + 1)
                    next_level.add(num - 1)
            res += 1

            level = next_level
        return res
