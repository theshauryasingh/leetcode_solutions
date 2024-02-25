# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finalList = ListNode()
        cur = finalList
        while(1):
            smallest = float(inf)
            index = -1
            for i, l in enumerate(lists):
                if l!= None and l.val < smallest:
                    smallest = l.val
                    index = i
            if index == -1:
                 break
            cur.next = ListNode(smallest)
            lists[index] = lists[index].next
            cur = cur.next
        return finalList.next