# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        cur = head
        nex = cur.next
        temp = nex.next
        while(temp):
            nex.next  = temp.next
            temp.next = cur.next
            cur.next = temp
            if nex.next != None:
                cur = cur.next
                nex = nex.next
            temp = nex.next
        return head