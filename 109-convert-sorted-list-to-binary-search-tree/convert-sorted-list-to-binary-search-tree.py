# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def middleOfList(self, head, last):
        slow = head
        fast = head
        while(fast != last and fast.next != last):
            slow = slow.next
            fast = fast.next.next
        # print(head.val, last, slow.val)
        return slow
    
    def solve(self, head, last):
        if head == last:
            return None
        root = self.middleOfList(head, last)
        # print(" leftsubtree ", head.val, root.val)
        leftsubtree = self.solve(head, root)
        # print(" rightsubtree ", root.next.val, last)
        rightsubtree = self.solve(root.next, last)
        return TreeNode(root.val, leftsubtree, rightsubtree)
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        root = self.solve(head, None)
        return root
