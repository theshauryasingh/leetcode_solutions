# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMid(self, l, r):
        mid = int((l+r)/2)
        return mid
    
    def arrayToBst(self, l,r):
        if l==r:
            return None
        if r-l == 1:
            return TreeNode(self.nums[l])
        mid = self.getMid(l,r)
        root = self.nums[mid]
        leftsubtree = self.arrayToBst(l,mid)
        rightsubtree = self.arrayToBst(mid+1,r)
        return TreeNode(root, leftsubtree, rightsubtree)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        bst = self.arrayToBst(0,len(self.nums))
        return bst
            