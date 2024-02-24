"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        maxDepth = 0
        for child in root.children:
            depth = self.maxDepth(child)
            if depth > maxDepth:
                maxDepth = depth
        return 1 + maxDepth