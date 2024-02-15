# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getVal(self, root):
        if root == None:
            return
        self.values.append(root.val)
        l = root.left
        r = root.right
        self.getVal(l)
        self.getVal(r)
        return
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.values = []
        self.getVal(root)
        self.values.sort()
        diff_array = []
        for i in range(len(self.values)-1):
            diff_array.append(self.values[i+1] - self.values[i])
        diff_array.sort()
        # print(self.values, diff_array)
        return diff_array[0]
        # l = root.left
        # r = root.right
        # while(l!=None or r!=None):
        #     a = l.val
        #     b = r.val
        #     if a!=None
        #         values.append(a)
        #     if b!=None
        #         values.append(b)
            
            
        