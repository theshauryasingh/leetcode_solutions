# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        visited = []
        stack = [root]
        while(stack):
            item = stack.pop()
            if item.val not in self.item.keys():
                self.item[item.val] = 1
            else:
                self.item[item.val] += 1
            if item.right != None:
                stack.append(item.right)
            if item.left != None:
                stack.append(item.left)
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # mode   - most occured element
        # mean   - average
        # median - middle value
        self.item = {}
        self.dfs(root)
        print(self.item)
        answer = []
        max = float('-inf')
        for key, val in self.item.items():
            if val > max :
                max = val
        for key, val in self.item.items():
            if val == max :
                answer.append(key)
        return answer
        