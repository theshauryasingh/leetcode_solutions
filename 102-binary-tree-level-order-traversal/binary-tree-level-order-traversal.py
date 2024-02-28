# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        queue = [(root,0)]
        curDepth = 0
        temp = []
        while(len(queue)!=0):
            item, depth = queue.pop(0)
            if depth > curDepth:
                self.answer.append(temp)
                temp = []
                curDepth +=1
            temp.append(item.val)
            if item.left != None:
                queue = queue + [(item.left, depth+1)]
            if item.right != None:
                queue = queue + [(item.right, depth+1)]
        if len(temp)>0:
            self.answer.append(temp)
    
    def solve(self, root):
        if root == None:
            return
        # if root.left != None and root.right != None:
        #     return [[root.val], [root.left.val, root.right.val]]
        # elif root.left == None and root.right == None:
        #     return [[root.val]]
        # else:
        #     return [[root.val], self.solve(root.left), self.solve(root.right) ]
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        self.answer = []
        self.bfs(root)
        return self.answer 
    
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         a = self.bfs(root)
#         print(a)
#         return [a]
    
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