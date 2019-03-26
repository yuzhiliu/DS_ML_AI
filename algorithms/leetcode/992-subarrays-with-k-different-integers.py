class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.at_most_k(A, K) - self.at_most_k(A, K - 1)

    def at_most_k(self, A, K):
        l, r = 0, 0
        n = len(A)
        count = {}
        res = 0
        while l <= r and r < n:
            count[A[r]] = count.get(A[r], 0) + 1
            while len(count) > K:
                count[A[l]] -= 1
                if count[A[l]] == 0:
                    del count[A[l]]
                l += 1
            res +=  - l + 1
            r += 1
        return res
