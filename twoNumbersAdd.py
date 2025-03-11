# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = l1
        curr2 = l2
        list1 = []
        list2 = []

        #reversse them, add them together then reverse it
        #output it as linked list
        
        while(curr):
            list1.append(curr.val)
            curr = curr.next
        
        while(curr2):
            list2.append(curr2.val)
            curr2 = curr2.next
        
        list1.reverse()
        list2.reverse()
        num1 = int(''.join(str(num) for num in list1))
        num2 = int(''.join(str(num) for num in list2))
        num_total = num1 + num2
        string_num_total = str(num_total)

        list_total = list(string_num_total)
        list_total.reverse()
        list_nodes = []

        for num in list_total:
            list_nodes.append(ListNode(int(num),None))
        for i in range((len(list_nodes))-1):
            list_nodes[i].next = list_nodes[i+1]
        node = list_nodes[0]
        return node
            

        


