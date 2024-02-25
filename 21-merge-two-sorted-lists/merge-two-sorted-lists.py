# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        finalList = ListNode()
        cur = finalList
        while(list1 and list2):
            if list1.val > list2.val:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            else:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return finalList.next
        
        