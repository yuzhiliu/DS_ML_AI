class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if self.can_eat(piles, m, H):
                r = m 
            else:
                l = m + 1
        return l
    
    def can_eat(self, piles, m, H):
        cnt = 0
        for p in piles:
            cnt += p // m if p % m == 0 else p // m + 1
            if cnt > H:
                return False
        return True
