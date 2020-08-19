# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # BFS
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        current = [root]

        reverse = False
        while current:
            next_level = []
            vals = []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            if reverse:
                res.append(vals[::-1])
            else:
                res.append(vals)
            reverse = not reverse
        return res

    # BFS
    # https://discuss.leetcode.com/topic/25135/python-simple-bfs/2
    def zigzagLevelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        temp = []
        queue = [root]
        flag = 1

        while queue:
            vals = []
            for i in range(len(queue)):
                node = queue.pop(0)
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(vals[::flag])
            flag *= -1
        return res





if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print Solution().zigzagLevelOrder(root)
    print Solution().zigzagLevelOrder2(root)

