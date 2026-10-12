# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        nextPointer = head
        while n > 0:
            nextPointer = nextPointer.next 
            n -= 1
        prevPointer = dummyNode
        while nextPointer:
            prevPointer = prevPointer.next
            nextPointer = nextPointer.next
        nextPointer = prevPointer.next
        prevPointer.next = nextPointer.next
        return dummyNode.next