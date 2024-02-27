# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self, root, node):
        if root == None:
            return 0
        if root.val == node:
            return 1
        a = self.level(root.left,  node)
        if a > 0:
            return a +1
        a = self.level(root.right, node)
        if a > 0:
            return a +1
        return 0
        
    def parent(self, root, node):
        if root == None:
            return 
        parent = None
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.right:
                stack.append(temp.right)
                if temp.right.val == node:
                    parent = temp
            if temp.left:
                stack.append(temp.left)
                if temp.left.val == node:
                    parent = temp
        return parent
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        a = self.level(root, x)
        b = self.level(root, y)
        print(a, b)
        c = self.parent(root, x)
        d = self.parent(root, y)
            
        return a == b and c != d