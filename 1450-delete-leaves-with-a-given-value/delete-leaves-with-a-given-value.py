# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs():
        pass
    
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root != None and root.left == None and root.right == None and root.val == target:
            return None
        else:
            if root.left != None:
                l = self.removeLeafNodes(root.left, target)
                root.left = l
            if root.right != None:
                r = self.removeLeafNodes(root.right, target)
                root.right = r
            if root.left == None and root.right == None and root.val == target:
                return None
            return root
        
        