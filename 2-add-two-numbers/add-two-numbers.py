# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a  = l1.val
        b  = l2.val
        cursum = a + b 
        head = ListNode(cursum%10)
        carry = int(cursum/10)
        l3 = head
        cur = l3
        l1 = l1.next
        l2 = l2.next
        while(l1 != None or l2 != None):
            a  = l1.val if l1 else 0
            b  = l2.val if l2 else 0
            cursum = a + b + carry
            cur.next = ListNode(cursum%10)
            carry = int(cursum/10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # print(a,b,cursum,carry, l1, l2)
        if carry > 0:
            cur.next = ListNode(carry)
            cur = cur.next
        return l3
    
    
## approach I - wrong understanding(thought of writing answer in reverse)
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         stack1 = []
#         stack2 = []
#         while(l1 != None):
#             stack1.append(l1.val)
#             l1 = l1.next
#         while(l2 != None):
#             stack2.append(l2.val)
#             l2 = l2.next
#         a  = stack1.pop()
#         b  = stack2.pop()
#         cursum = a + b 
#         head = ListNode(cursum%10)
#         carry = int(cursum/10)
#         l3 = head
#         cur = l3
#         while(len(stack1) != 0 or len(stack2) != 0):
#             a = stack1.pop() if stack1 else 0
#             b = stack2.pop() if stack2 else 0
#             cursum = a + b + carry
#             print(a,b,cursum)
#             cur.next = ListNode(cursum%10)
#             carry = int(cursum/10)
#             cur = cur.next
#         if carry > 0:
#             cur.next = ListNode(carry)
#             cur = cur.next
#         return l3
            
            