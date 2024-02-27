# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minNode = float(inf)
        secMinNode = float(inf)
        stack = [root]
        while(stack):
            node = stack.pop()
            # print(node.val, minNode, secMinNode)
            if node.val < minNode:
                secMinNode = minNode
                minNode = node.val
            elif node.val!= minNode and node.val < secMinNode:
                secMinNode = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if secMinNode == float(inf):
            return -1
        # print("-------- ", secMinNode)
        return secMinNode
                