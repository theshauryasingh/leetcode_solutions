"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randomPointerList = []
        finalList = Node(-1)
        cur = finalList
        org = head
        while(org):
            cur.next = Node(org.val)
            cur = cur.next
            # print(cur, cur.val, cur.next, cur.random)
            randomPointerList.append(cur)
            org = org.next
        cur = finalList
        while(head):
            if head.random:
                # print(head.val)
                index = 0
                temp = head.random
                while(temp):
                    temp = temp.next
                    index += 1
                cur.next.random = randomPointerList[len(randomPointerList) - index]
            cur = cur.next
            head = head.next
        return finalList.next
        