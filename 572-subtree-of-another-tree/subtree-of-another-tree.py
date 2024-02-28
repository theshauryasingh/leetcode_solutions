# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def match(self, root, subRoot):
        # print(root, subRoot)
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val :
            return self.match(root.left, subRoot.left) and self.match(root.right, subRoot.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # [3,4,5,1,2]
        # [4,1,2]
        # [3,4,5,1,2,null,null,null,null,0]
        # [4,1,2]
        # [1,1]
        # [1]
        if root == None:
            return False
        if root.val == subRoot.val:
            if self.match(root, subRoot):
                print(root)
                print(subRoot)
                return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)