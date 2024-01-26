# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        current = head

        while current:
            if prev and prev.val > current.val:
                prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node

        return dummy.next
        