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

        if not head :
            return
        current = head

        #interweave the nodes the nodes by setting the next and inserting it
        while(current):
            temp = current.next
            current.next = Node(current.val,temp, None)
            current = temp
                
        current = head
        #set the random nodes by taking the current next random and setting it to the current random next
        while(current):
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        #create two new heads one for the old list and one for the the new list and keep the head of the new list
        cur_old = head
        cur_new = head.next
        copy_head = cur_new

        #while we can keep moving the oriiginal list froward just set it to the node aheads next then go to ur next and make sure that when you move forward for the new list you only do it if the original list is not yet null
        while(cur_old):
            cur_old.next = cur_new.next
            cur_old = cur_old.next
            if cur_old:
                cur_new.next = cur_old.next
                cur_new = cur_new.next
        return copy_head
        
