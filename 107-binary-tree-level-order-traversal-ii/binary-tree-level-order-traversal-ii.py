# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solveLevelOrderBottom(self, root):
        queue = [(root, 0)]
        curDepth = 0
        stack = []
        temp = []
        while(queue):
            node, depth = queue.pop(0)
            if depth > curDepth:
                stack.append(temp)
                temp = []
                curDepth += 1
            temp.append(node.val)
            if node.left != None:
                queue.append((node.left, depth+1))
            if node.right != None:
                queue.append((node.right, depth+1))
        if len(temp):
            stack.append(temp)
        while(stack):
            self.answer.append(stack.pop())
            
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        self.answer = []
        self.solveLevelOrderBottom(root)
        return self.answer