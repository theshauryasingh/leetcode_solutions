# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = [[root,1]]
        minDepth = float(inf)
        while(stack):
            node, depth = stack.pop()
            # print(node, depth)
            if node.left == None and node.right == None:
                if depth < minDepth :
                    minDepth = depth
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return minDepth
                
                 