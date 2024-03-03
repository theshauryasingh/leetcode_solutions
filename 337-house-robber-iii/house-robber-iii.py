# #input
# [3]
# [3,2,3]
# [3,2,3,null,3,null,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # root = [3,2,3,null,3,null,1]
        ans = self.solve(root)
        return max(ans[0], ans[1])
    
    def solve(self,root):
        if root == None:
            return (0,0)
        elif root.left == None and root.right == None:
            return (root.val,0)
        left = self.solve(root.left)
        right = self.solve(root.right)
        return (root.val + left[1] + right[1], max(left[0],left[1]) + max(right[0],right[1]))