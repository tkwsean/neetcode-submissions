# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            leftMax, rightMax = dfs(node.left), dfs(node.right)
            leftMax, rightMax = max(leftMax, 0), max(rightMax, 0)
            res[0] = max(res[0], leftMax+rightMax+node.val)
            return max(leftMax,rightMax)+node.val
        dfs(root)
        return res[0]