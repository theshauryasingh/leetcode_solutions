"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""  

class Solution:
    def solveLevelOrder(self,root):
        queue = [(root, 0)]
        curDepth = 0
        temp = []
        while(queue):
            node, depth = queue.pop(0)
            if depth > curDepth:
                self.answer.append(temp)
                temp = []
                curDepth+=1
            temp.append(node.val)
            for child in node.children:
                if child != None:
                    queue.append((child, depth+1))
        if len(temp) > 0:
            self.answer.append(temp)
            
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        self.answer = []
        self.solveLevelOrder(root)
        return self.answer