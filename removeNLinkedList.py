# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        fast, slow = dummy,dummy

        #this way it lands 1 before the one we want to remove
        
        for _ in range(n+1):
            fast = fast.next
        
        while(fast):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

