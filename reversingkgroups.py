# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,None)
        dummy.next = head

        current = head
        iteration = head
        prev = None
        group_prev = None
        while(True):
            for i in range(k):
                if iteration:
                    iteration = iteration.next
                else:
                    return dummy.next
            prev = iteration
            temp_current = current
            while(current != iteration):
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            if group_prev:
                group_prev.next = prev
            else:
                dummy.next= prev
            group_prev = temp_current
            current = iteration

