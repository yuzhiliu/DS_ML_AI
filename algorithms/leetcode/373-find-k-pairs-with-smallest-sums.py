import heapq
class Solution(object):
    # simple sort
    # Time O(n^2*log(n)); Space O(n^2)
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        lst = [(i + j, i, j) for i in nums1 for j in nums2]
        lst.sort()
        return [[i, j] for v, i, j in lst[:k]]

    # heap
    # Time O(n^2*log(k)); Space O(k)
    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        res = []
        n1, n2 = len(nums1), len(nums2)
        while len(res) < k and heap:
            v, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i +1 < n1 and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            if j +1 < n2 and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return res


    # O(n) solution?
if __name__ == '__main__':
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 3
    print Solution().kSmallestPairs(nums1,nums2,k)
    print Solution().kSmallestPairs2(nums1,nums2,k)
