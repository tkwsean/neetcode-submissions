# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        pointerOne = dummyNode
        pointerTwo = dummyNode
        while n > 0:
            pointerTwo = pointerTwo.next
            n -= 1
        while pointerTwo and pointerTwo.next != None:
            pointerOne = pointerOne.next
            pointerTwo = pointerTwo.next
        pointerOne.next = pointerOne.next.next
        return dummyNode.next