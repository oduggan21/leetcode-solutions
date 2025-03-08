# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return 

      
        slow = head
        fast = head.next

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        
        prev = None
        curr = slow.next
        slow.next = None

        while(curr):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        first, second = head, prev
        while(second):
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
        return head

        
