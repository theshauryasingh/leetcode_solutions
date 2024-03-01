# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, float('inf'), float('-inf'))
        
    def solve(self, root, lessthan, greaterthan):
        if root == None:
            return True
        if root.val >= lessthan:
            return False
        if root.val <= greaterthan:
            return False
        a = self.solve(root.left, root.val, greaterthan)
        b = self.solve(root.right, lessthan, root.val)
        return a and b