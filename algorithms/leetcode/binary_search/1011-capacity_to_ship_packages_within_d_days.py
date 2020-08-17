class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if self.can_ship_in_D_days(weights, m, D):
                r = m
            else:
                l = m + 1
        return l
    
    def can_ship_in_D_days(self, weights, m, D):
        cnt = 0
        days = 1
        for w in weights:
            cnt += w
            if cnt > m:
                cnt = w
                days += 1
            if days > D:
                return False
        return True
