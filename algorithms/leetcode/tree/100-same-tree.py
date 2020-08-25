# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [[p, q]]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            else:
                if n1.val != n2.val:
                    return False
                stack.append([n1.left, n2.left])
                stack.append([n1.right, n2.right])
        return True

    import collections
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = collections.deque()
        queue.append([p, q])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            else:
                if n1.val != n2.val:
                    return False
                queue.append([n1.left, n2.left])
                queue.append([n1.right, n2.right])
        return True
