# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [[root, float('-inf'), float('inf')]]
        while stack:
            
            node, lower, upper = stack.pop()
            if node:
                if node.val <= lower or node.val >= upper:
                    return False
                stack.append([node.left, lower, node.val])
                stack.append([node.right, node.val, upper])
        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))
        
    def dfs(self, node, lower, upper):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return self.dfs(node.left, lower, node.val) and self.dfs(node.right, node.val, upper)


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        vals = []
        self.in_order(root, vals)
        prev = vals[0]
        for v in vals[1:]:
            if v <= prev:
                return False
            prev = v
        return True
    def in_order(self, node, vals):
        if node.left:
            self.in_order(node.left, vals)
        if node:
            vals.append(node.val)
        else:
            return
        if node.right:
            self.in_order(node.right, vals)


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
       
        vals = self.in_order(root)
        prev = vals[0]
        for v in vals[1:]:
            if v <= prev:
                return False
            prev = v
        return True
    
    def in_order(self, node):
        if node is None:
            return []
        return self.in_order(node.left) + [node.val] + self.in_order(node.right)
