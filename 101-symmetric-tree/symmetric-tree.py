# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkIsSymmetric(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val == root2.val:
            return self.checkIsSymmetric(root1.left, root2.right) and self.checkIsSymmetric(root1.right, root2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkIsSymmetric(root.left, root.right)

#failed attempt
# class Solution:
#     def bfs(self, root):
#         visited = [root.val]
#         queue = [root]
#         while(len(queue)!=0):
#             item = queue.pop(0)
#             if item.left != None:
#                 queue = queue + [item.left]
#             if item.left != None:
#                 queue = queue + [item.right]
#             if item.val not in visited:
#                 visited.append(item.val)
#         return visited
        
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         a = self.bfs(root.left)
#         b = self.bfs(root.right)
#         print(a,b)
#         return a == b