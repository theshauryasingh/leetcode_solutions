# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, depth):
        if root == None:
            return None
        if root.left == None and root.right == None:
            self.max = max(self.max, depth)
        self.solve(root.left, depth + 1)
        self.solve(root.right, depth + 1)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.max = 0
        self.solve(root, 1)
        return self.max
        
        
        
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root == None:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))